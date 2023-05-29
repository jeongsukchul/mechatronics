import numpy as np
from scipy.interpolate import Rbf

import plotly.graph_objects as go
import pandas as pd

# Read data from Excel file
data_frame = pd.read_excel('all_data.xlsx')

# Extract x, y, and z values
x = data_frame['pwm'].values
y = data_frame['battery_voltage'].values
z = data_frame['thrust'].values
# Print the extracted data
print("x")
print(x)
print("y")
print(y)
print("z")
print(z)

# Define the interpolation function using Rbf
interp = Rbf(x, y, z, function='thin_plate')

# Generate a regular grid for interpolation
xi, yi = np.meshgrid(np.linspace(0, 1, 100), np.linspace(0, 1, 100))

# Perform the interpolation
zi = interp(xi, yi)

# Print interpolated values at specific points
print(interp(0.25, 0.25))
print(interp(0.5, 0.5))
# Access the coefficients and nodes
coefficients = interp.nodes
print("coeffi")
print(coefficients)
# Create a surface plot

fig = go.Figure(data=[go.Surface(x=xi, y=yi, z=zi)])

# Set the plot title and axis labels
fig.update_layout(title='Biharmonic Interpolation Mesh', scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))

# Show the plot
fig.show()