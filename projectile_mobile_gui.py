import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 10  #gravitational constant

# Initial conditions
u = 180 #initial velocity
theta = 60 #Enter launch angle in degrees
theta_rad = np.deg2rad(theta)
v0x = u * np.cos(theta_rad)
v0y = u * np.sin(theta_rad)
x0 = 0.0
y0 = 0.0

# Time step and duration
dt = 0.01
t_max = 32#simulation time

# Initialize arrays to store data
t_values = [0]
x_values = [x0]
y_values = [y0]

# Initialize variables to track highest point
highest_point = y0
highest_point_time = 0

# Initialize variables to track when y = 0
y_equals_zero_time = None
y_equals_zero_x = None

# Simulation loop
x = x0
y = y0
vx = v0x
vy = v0y
t = 0

while t <= t_max:
    t += dt
    x += vx * dt
    y += vy * dt
    vy -= g * dt
    t_values.append(t)
    x_values.append(x)
    y_values.append(y)

    # Update highest point information
    if y > highest_point:
        highest_point = y
        highest_point_time = t

    # Check for y = 0
    if y <= 0 and y_values[-2] > 0:
        y_equals_zero_time = t
        y_equals_zero_x = x

# Print the user-provided information
print(f"Initial Velocity: {u} m/s")
print(f"Launch Angle: {theta} degrees")
print(f"Gravitational Constant: {g} m/s^2")
print(f"Maximum Simulation Time: {t_max} seconds\n")

# Print the simulation results
print("--------   Simulation Data     ----------\n")
print(f"Highest Point Reached: {highest_point:.2f} meters")
print(f"Time at Highest Point: {highest_point_time:.2f} seconds")
print(f"Time when y = 0: {y_equals_zero_time:.2f} seconds")
print(f"Horizontal Position (x) when y = 0: {y_equals_zero_x:.2f} meters")

# Plot the trajectory
plt.figure()
plt.plot(x_values, y_values)
plt.title('Projectile Motion with Gravity')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.grid(True)
plt.show()
