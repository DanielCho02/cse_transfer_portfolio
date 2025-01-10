# A program that generate theoretical centripetal force graph
import matplotlib.pyplot as plt
import numpy as np

# Generate x data representing angular speed (rad/s)
x = np.arange(0, 8, 0.1)

# Generate y data representing theoretical centripetal force based on F = m * r * omega^2
# where m is assumed to be constant, and r (radius) is different for each curve
y1 = 0.012 * x**2  # Theoretical force for radius = 0.08m
y2 = 0.0165 * x**2  # Theoretical force for radius = 0.11m
y3 = 0.021 * x**2  # Theoretical force for radius = 0.14m
y4 = 0.0255 * x**2  # Theoretical force for radius = 0.17m

# Plot the theoretical centripetal force curves
plt.plot(x, y1, color='red', label='0.08m')
plt.plot(x, y2, color='blue', label='0.11m')
plt.plot(x, y3, color='green', label='0.14m')
plt.plot(x, y4, color='orange', label='0.17m')

# Add labels for axes and legend
plt.xlabel("Angular Speed (rad/s)")
plt.ylabel("Force (N)")
plt.legend()

# Save the graph as a PNG file and display it
plt.savefig("C:/Users/danie/OneDrive/바탕 화면/python workspace/data/graph.png")
plt.show()