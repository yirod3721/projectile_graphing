import numpy as np
import matplotlib.pyplot as plt
print("--------------------_The Drag Simulation_--------------------")
# Constants
g = float(input("Enter gravitational constant (m/s^2): "))  # Acceleration due to gravity (m/s^2)

# Parameters for air resistance (customize these values)
rho = 1.225  # Air density (kg/m^3)
A = 0.6205  # Cross-sectional area (m^2)
Cd = 0.705  # Drag coefficient

# Initial conditions
u = float(input("Enter initial velocity in m/s: "))
theta = float(input("Enter launch angle in degrees: "))
theta_rad = np.deg2rad(theta)
v0x = u * np.cos(theta_rad)
v0y = u * np.sin(theta_rad)
x0 = 0.0
y0 = 0.0

# Time step and duration
dt = 0.01
t_max = float(input("Enter maximum simulation time (s): "))

# Initialize arrays to store data
t_values = [0]
x_values = [x0]
y_values = [y0]
speed_values = [u]
distance_values = [0]
answer = bool(False)
# Simulation loop
x = x0
y = y0
vx = v0x
vy = v0y
t = 0
y_equals_zero_time = None
y_equals_zero_x = None
half_given_time = t_max / 2 + 5  # Half of the given time + 5 seconds
rho_sea_level = 1.225
while t <= t_max:
    t += dt

    # Calculate the magnitude of the velocity
    v = np.sqrt(vx**2 + vy**2)

    # Calculate the drag forces
    F_drag_x = -0.5 * rho * A * Cd * v * vx
    F_drag_y = -0.5 * rho * A * Cd * v * vy

    # Update the acceleration due to gravity and air resistance
    ax = F_drag_x / u  # Assuming a constant mass 'u'
    ay = (-u * g + F_drag_y) / u

    # Update velocity
    vx += ax * dt
    vy += ay * dt

    # Update position
    x += vx * dt
    y += vy * dt
    t_values.append(t)
    x_values.append(x)
    y_values.append(y)

    # Calculate speed and distance
    speed = np.sqrt(vx**2 + vy**2)
    distance = x
    speed_values.append(speed)
    distance_values.append(distance)

    if y <= 0 and y_values[-2] > 0:
        y_equals_zero_time = t
        y_equals_zero_x = x
        # Check if the altitude is 12,000 meters or more
    if y >= 12000:
        # Adjust air density to 18% of sea level air density
        rho = 0.18 * rho_sea_level
    else:
        rho = rho_sea_level
    if t >= half_given_time and y <= 0 and answer == False:
        user_input = input("Reached y = 0 at half of the given time + 5 seconds. Continue simulation? (yes/no): ")
        if user_input.lower() == "no":
            break
        answer = bool(True)
    

# Print the user-provided information
print(f"Initial Velocity: {u} m/s")
print(f"Launch Angle: {theta} degrees")
print(f"Gravitational Constant: {g} m/s^2")
print(f"Air Density: {rho} kg/m^3")
print(f"Cross-Sectional Area: {A} m^2")
print(f"Drag Coefficient: {Cd}")
print(f"Maximum Simulation Time: {t_max} seconds\n")

# Print the simulation results
print("--------   Simulation Data     ----------\n")
print(f"Highest Point Reached: {max(y_values):.2f} meters")
print(f"Time at Highest Point: {t_values[y_values.index(max(y_values))]:.2f} seconds")
print(f"Time when y = 0: {y_equals_zero_time:.2f} seconds")
print(f"Horizontal Position (x) when y = 0: {y_equals_zero_x:.2f} meters")
print(f"Horizontal Distance Traveled: {max(x_values):.2f} meters")
print(f"Total Flight Time: {t_values[-1]:.2f} seconds")

# Plot the trajectory
plt.figure()
plt.plot(x_values, y_values)
plt.title('Projectile Motion with Air Resistance')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.grid(True)
plt.show()

# Interactive input loop
while True:
    user_input = input("Enter a time value (or ':q' to quit): ")
    
    if user_input == ":q":
        break  # Exit the loop if the user enters ":q"
    
    try:
        user_time = float(user_input)
        print(t_max)
        print(user_time)
        if 0 <= user_time <= t_max:
            # Interpolate x, y, speed, and distance at the user-provided time
            index = int(user_time / dt)
            user_x = x_values[index]
            user_y = y_values[index]
            user_speed = speed_values[index]
            user_distance = distance_values[index]
            print(f"At t = {user_time:.2f} seconds:")
            print(f"- Horizontal Position (x): {user_x:.2f} meters")
            print(f"- Vertical Position (y): {user_y:.2f} meters")
            print(f"- Speed: {user_speed:.2f} m/s")
            print(f"- Distance Traveled: {user_distance:.2f} meters")
        else:
            print("Time value must be in the range [0, t_max].")
            print(t_max)
            print(user_time)
    except ValueError:
        print("Invalid input. Enter a valid time or ':q' to quit.")
