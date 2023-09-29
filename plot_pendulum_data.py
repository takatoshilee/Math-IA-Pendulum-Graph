import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Read data from the file
data = np.loadtxt("pendulum_data.txt")

# Extract angles, lengths, and percentage errors
angles = data[:, 0]
percent_errors = data[:, 2]

# Define a quadratic function for curve fitting
def quadratic_function(x, a, b, c):
    return a * x**2 + b * x + c

# Perform the curve fit
popt, pcov = curve_fit(quadratic_function, angles, percent_errors)

# Generate data points for the fitted curve
fit_curve = quadratic_function(angles, *popt)

# Create a plot
plt.scatter(angles, percent_errors, label='Data')
plt.plot(angles, fit_curve, label='Fitted Curve', color='red')
plt.xlabel('Initial Angle (Degrees)')
plt.ylabel('Percent Error')
plt.title('Fitted Quadratic Curve for Percent Error vs. Initial Angle')
plt.legend()
plt.grid(True)
plt.show()

# Display the fitted coefficients
print("Fitted coefficients:", popt)
