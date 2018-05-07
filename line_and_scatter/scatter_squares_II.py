import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# example of custom colors. rgb values can be used as well
# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)

# colormaps can be used to emphasize a pattern in data
# below, we assign a colormap based on the points' y-value
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# set range for each axis
plt.axis([0, 1100, 0, 1100000])

# set size of tick labels
plt.tick_params(axis = 'both', which = 'major', labelsize=14)

plt.show()

# additionally, if we wanted to save the plot to a file
# instead of simply displaying it, replace the call to
# plt.show() with plt.savefig
# ex
# plt.savefig('path', bbox_inches='tight')
# the second parameter, bbox_inches crops the extra whitespace from
# around the plot
