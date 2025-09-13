import numpy as np
import matplotlib.pyplot as plt

print("--------------------_The Drag Simulation_--------------------")

# Constants
g = float(input("Enter gravitational constant (m/s^2): "))  # Acceleration due to gravity (m/s^2)

# Parameters for air resistance
rho_sea_level = 1.225  # Air density at sea level (kg/m^3)
rho = rho_sea_level  # Variable air density that can change with altitude
A = 0.6205  # Cross-sectional area of the projectile (m^2)
Cd = 0.705  # Drag coefficient
m = float(input("Enter the mass of the projectile (kg): "))  # Mass of the projectile

# Initial conditions
u = float(input("Enter initial velocity in m/s: "))
theta = float(input("Enter launch angle in degrees: "))
theta_rad = np.deg2rad(theta)  # Convert angle to radians
v0x = u * np.cos(theta_rad)  # Initial horizontal velocity
v0y = u * np.sin(theta_rad)  # Initial vertical velocity
x0 = 0.0  # Initial horizontal position
y0 = 0.0  # Initial vertical position

# Time step and duration
dt = 0.01  # Time step for the simulation (s)
t_max = float(input("Enter maximum simulation time (s): "))
half_max_time = t_max / 2  # Calculate half of the maximum time

# Initialize arrays to store data
t_values = [0]
x_values = [x0]
y_values = [y0]
speed_values = [u]
distance_values = [0]

# Simulation loop
x = x0
y = y0
vx = v0x
vy = v0y
t = 0
y_equals_zero_time = None
y_equals_zero_x = None
stop_simulation = False  # Variable to control whether to stop the simulation

while t <= t_max and not stop_simulation:
    t += dt

    # Calculate the magnitude of the velocity
    v = np.sqrt(vx**2 + vy**2)

    # Calculate the drag forces
    F_drag_x = -0.5 * rho * A * Cd * v * vx
    F_drag_y = -0.5 * rho * A * Cd * v * vy

    # Update the acceleration due to gravity and air resistance
    ax = F_drag_x / m  # Acceleration in the x-direction
    ay = (-m * g + F_drag_y) / m  # Acceleration in the y-direction

    # Update velocity
    vx += ax * dt
    vy += ay * dt

    # Update position
    x += vx * dt
    y += vy * dt

    # Store the results
    t_values.append(t)
    x_values.append(x)
    y_values.append(y)
    speed = np.sqrt(vx**2 + vy**2)
    distance = x
    speed_values.append(speed)
    distance_values.append(distance)

    # Check if the projectile reaches the ground
    if y <= 0 and y_values[-2] > 0:
        y_equals_zero_time = t
        y_equals_zero_x = x
        
        # Check if the projectile lands before half of the maximum time
        if t <= half_max_time:
            user_input = input(f"The projectile landed at y = 0 at t = {t:.2f} seconds, before half of the simulation time. Do you want to stop the simulation? (yes/no): ")
            if user_input.lower() == "yes":
                stop_simulation = True
                print("Simulation stopped early based on user input.")
            else:
                print("Continuing the simulation...")

    # Adjust air density if altitude is 12,000 meters or more
    if y >= 12000:
        rho = 0.18 * rho_sea_level  # Reduced air density at high altitude
    else:
        rho = rho_sea_level  # Reset air density to sea level value

# Print the user-provided information
print(f"\nInitial Velocity: {u} m/s")
print(f"Launch Angle: {theta} degrees")
print(f"Gravitational Constant: {g} m/s^2")
print(f"Mass of the Projectile: {m} kg")
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

# Interactive input loop for querying projectile state at specific times
while True:
    user_input = input("Enter a time value (or ':q' to quit): ")

    if user_input == ":q":
        break  # Exit the loop if the user enters ":q"

    try:
        user_time = float(user_input)
        # Keep asking for valid input if the time is outside the range [0, t_max]
        while user_time < 0 or user_time > t_max:
            print(f"Time value must be in the range [0, {t_max}].")
            user_time = float(input(f"Please enter a valid time between 0 and {t_max} seconds: "))

        # Find the closest index for the provided time
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
    except ValueError:
        print("Invalid input. Enter a valid time or ':q' to quit.")
