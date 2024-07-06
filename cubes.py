import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues)

# Set chart title and label axes.
ax.set_title("Cubed Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis="both", which="major", labelsize=14)

# Set the range for each axis.
ax.axis([0, 5000, 0, 130000000000])
plt.show()

5000**3
