import numpy as np
import matplotlib.pyplot as plt

# Load data from the C++ program's output file
data = np.loadtxt("pendulum_data.txt")

# Extract angles, lengths, and percentage errors
angles = data[:, 0]
lengths = data[:, 1]
percent_errors = data[:, 2]

# Choose a specific length for the 2D heatmap
target_length = 2.0  # Adjust this to the desired length

# Filter data for the chosen length
mask = (lengths == target_length)
filtered_angles = angles[mask]
filtered_percent_errors = percent_errors[mask]

# Create a 2D heatmap plot for the chosen length
plt.figure(figsize=(10, 6))
plt.scatter(filtered_angles, filtered_percent_errors, c=filtered_percent_errors, cmap='viridis', s=50)
plt.xlabel('Initial Angle (Degrees)')
plt.ylabel('Percent Error')
plt.title(f'2D Heatmap of Percent Error vs. Initial Angle (Length={target_length}m)')
plt.colorbar(label='Percent Error')
plt.show()
