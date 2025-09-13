import numpy as np
import matplotlib.pyplot as plt

# Constants
g = float(input("Enter gravitational constant (m/s^2): "))
u = float(input("Enter initial velocity in m/s: "))
dt = 0.001  # Small time step

theta_range = np.linspace(0, np.pi / 2, 91)  # Angles from 0 to 90 degrees

# Variables to track best angles
best_height = 0
best_height_angle = 0
best_range = 0
best_range_angle = 0

optimal_angle = 45  # We know 45° is the theoretical optimal angle for range
optimal_trajectory = None
highest_trajectory = None
farthest_trajectory = None

# Iterate over all angles
def simulate_trajectory(theta_rad):
    x, y = 0.0, 0.0
    vx, vy = u * np.cos(theta_rad), u * np.sin(theta_rad)
    t = 0
    
    x_values, y_values = [], []
    max_height = 0
    
    while y >= 0:
        x_values.append(x)
        y_values.append(y)
        
        if y > max_height:
            max_height = y
        
        x += vx * dt
        y += vy * dt
        vy -= g * dt
        t += dt
    
    return max_height, x_values, y_values

for theta in theta_range:
    theta_rad = np.deg2rad(theta)
    height, x_vals, y_vals = simulate_trajectory(theta_rad)
    distance = x_vals[-1]  # Last x value is the range
    
    # Track highest point
    if height > best_height:
        best_height = height
        best_height_angle = theta
        highest_trajectory = (x_vals, y_vals)
    
    # Track farthest distance
    if distance > best_range:
        best_range = distance
        best_range_angle = theta
        farthest_trajectory = (x_vals, y_vals)
    
    # Track optimal 45-degree trajectory
    if np.isclose(theta, optimal_angle, atol=1e-2):
        optimal_trajectory = (x_vals, y_vals)

# Print results
print("\n--------   Simulation Data     ----------\n")
print(f"Highest Point Reached: {best_height:.2f} meters at {best_height_angle:.2f}°")
print(f"Farthest Distance Reached: {best_range:.2f} meters at {best_range_angle:.2f}°")
if optimal_trajectory:
    print(f"Optimal Theoretical Angle (45°) Range: {optimal_trajectory[0][-1]:.2f} meters")
else:
    print("No trajectory found for 45° angle.")

# Plot the three chosen trajectories
plt.figure(figsize=(8, 5))
plt.plot(*highest_trajectory, label=f"Highest ({best_height_angle:.2f}°)")
plt.plot(*farthest_trajectory, label=f"Farthest ({best_range_angle:.2f}°)")
if optimal_trajectory:
    plt.plot(*optimal_trajectory, label=f"Optimal (45°)", linestyle='dashed')
plt.axhline(0, color="black", linestyle="--", linewidth=0.8)  # Ground line
plt.title("Projectile Motion with Different Angles")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.legend()
plt.grid(True)
plt.show()
