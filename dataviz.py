#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import sys

# Get the file name, X variable, Y variable, and plot type from the command line
file_name = sys.argv[1]
x_variable = sys.argv[2]
y_variable = sys.argv[3]
plot_type = sys.argv[4]

# Read CSV file into a DataFrame
df = pd.read_csv(file_name)

# Plot the X and Y variables
df.plot(x=x_variable, y=y_variable, kind=plot_type)
plt.xlabel(x_variable)
plt.ylabel(y_variable)
plt.title(f"{y_variable} vs {x_variable}")
plt.xticks(rotation=45)
# Show the plot
# plt.show()
plt.savefig(f"{y_variable}_vs_{x_variable}.png", dpi=300, bbox_inches='tight')


