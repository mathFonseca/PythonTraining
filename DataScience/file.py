# Owner: Matheus Fonseca
# github: mathFons
# Created based on Data Science: Data Visualization with Python course on Udemy.

# Libraries

import matplotlib.pyplot as plt

# Data Sets

x_axis_values = [4, 5, 9, 14, 7, 19, 23, 2]
y_axis_values = [7, 16, 25, 43, 36, 32, 31, 1]

# Graphics Settings
graphic_title = "Data Visualization"
x_axis_title = "X Axis"
y_axis_title = "Y Axis"

graphic_color = "#000000"
graphic_linestyle = "--"
graphic_label = "Random Text"
graphic_dots_color = "b"
graphic_mark_type = "^"
graphic_dots_size = 100

plt.title(graphic_title)    
plt.xlabel(x_axis_title)
plt.ylabel(y_axis_title)

# Graphic Plotation

plt.plot(x_axis_values, y_axis_values, color=graphic_color, linestyle=graphic_linestyle)
plt.scatter(x_axis_values, y_axis_values, label=graphic_label, color=graphic_dots_color, marker=graphic_mark_type, s=graphic_dots_size)
plt.legend()
plt.show()



