import numpy as np
import matplotlib.pyplot as plt

# Constants
g = float(input("Enter gravitational constant (m/s^2): "))

# Initial conditions
u = float(input("Enter initial velocity in m/s: "))
theta = float(input("Enter launch angle in degrees: "))
theta_rad = np.deg2rad(theta)
v0x = u * np.cos(theta_rad)
v0y = u * np.sin(theta_rad)

# Time step and initial estimate
dt = 0.001
t_max = float(input("Enter maximum simulation time (s): "))
initial_steps = int(t_max / dt) + 1  # Initial estimate

# Preallocate arrays with some extra buffer
buffer_size = 2  # How much we expand each time
t_values = np.zeros(initial_steps)
x_values = np.zeros(initial_steps)
y_values = np.zeros(initial_steps)

# Initialize variables
x, y = 0.0, 0.0
vx, vy = v0x, v0y
t = 0
i = 0  # Array index

# Highest point tracking
highest_point = y
highest_point_time = 0

# Ground hit tracking
y_equals_zero_time = None
y_equals_zero_x = None

# Simulation loop (mainly for collecting data)
while t <= t_max:
    if i >= len(t_values):  # Check if we need to expand
        new_size = len(t_values) * buffer_size  # Double the size
        t_values = np.resize(t_values, new_size)
        x_values = np.resize(x_values, new_size)
        y_values = np.resize(y_values, new_size)

    t_values[i] = t
    x_values[i] = x
    y_values[i] = y

    # Update highest point
    if y > highest_point:
        highest_point = y
        highest_point_time = t

    # Check for y = 0 (ground hit)
    if y <= 0 and i > 0 and y_values[i - 1] > 0:
        y_equals_zero_time = t
        y_equals_zero_x = x
        user_choice = input("The projectile has hit the ground. Continue simulation? (y/n): ").strip().lower()
        if user_choice != 'y':
            break  # Stop the loop if the user chooses not to continue

    # Update motion
    x += vx * dt
    y += vy * dt
    vy -= g * dt
    t += dt
    i += 1  # Move to next index

# Trim arrays to actual size
t_values = t_values[:i]
x_values = x_values[:i]
y_values = y_values[:i]

# Print results
print(f"\nInitial Velocity: {u} m/s")
print(f"Launch Angle: {theta} degrees")
print(f"Gravitational Constant: {g} m/s^2")
print(f"Maximum Simulation Time: {t_max} seconds\n")

print("--------   Simulation Data     ----------\n")
print(f"Highest Point Reached: {highest_point:.2f} meters")
print(f"Time at Highest Point: {highest_point_time:.2f} seconds")
if y_equals_zero_time is not None:
    print(f"Time when y = 0: {y_equals_zero_time:.2f} seconds")
    print(f"Horizontal Position (x) when y = 0: {y_equals_zero_x:.2f} meters")

# Plot the trajectory
plt.figure()
plt.plot(x_values, y_values, label="Projectile Path")
plt.axhline(0, color="black", linestyle="--", linewidth=0.8)  # Ground line
plt.title("Projectile Motion with Gravity")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.legend()
plt.grid(True)
plt.show()

# Interactive input loop (ported from the first program)
while True:
    user_input = input("Enter a time value (or ':q' to quit): ")
    
    if user_input == ":q":
        break  # Exit the loop if the user enters ":q"
    
    try:
        user_time = float(user_input)
        if 0 <= user_time <= t_max:
            # Find the index corresponding to the user time
            index = int(user_time / dt)
            user_x = x_values[index]
            user_y = y_values[index]
            user_speed = np.sqrt(vx**2 + (vy + g * user_time)**2)
            print(f"At t = {user_time:.2f} seconds:")
            print(f"- Horizontal Position (x): {user_x:.2f} meters")
            print(f"- Vertical Position (y): {user_y:.2f} meters")
            print(f"- Speed: {user_speed:.2f} m/s")
        else:
            print("Time value must be in the range [0, t_max].")
    except ValueError:
        print("Invalid input. Enter a valid time or ':q' to quit.")
