#  -------------------------------------  Parametric Surface Plotting of a Cylinder  -------------------------------------------


# The parametric equation of a Cylinder is xi + rsin⁡θj + rcos⁡θk where r is the radius of the cylinder 
# and i,j,k being unit vectors in the direction of x-axis, y-axis, z-axis respectively.

# with 0 ≤ θ ≤ 2π 
# and h being the height of the cylinder, 0 < h ≤ 4

# Code:

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


theta = np.linspace(0, 2 * np.pi, 50) # setting the limitation on θ from 0 to 2π 

h = np.linspace(0, 4, 30) # setting the value of height = 4

theta_grid, x_grid = np.meshgrid(theta, h) 

y_grid = 5 * np.sin(theta_grid)

z_grid = 5 * np.cos(theta_grid)   

fig = plt.figure(figsize = (15,15))

ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x_grid, y_grid, z_grid, rstride = 2, cstride = 2, color = 'brown')

plt.show()
