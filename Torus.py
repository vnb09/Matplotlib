#  --------------------------------------  Parametric Surface Plotting of a Torus  ---------------------------------------------


# The parametric equation of a Toroid is (R + rcosθ)cosΦ i + (R + rcosθ)sinΦ j + rsinθ k where R,r > 0 
# R is the distance from the center of the tube to the center of the torus,
# r is the radius of the tube and i,j,k being unit vectors in the direction of x-axis, y-axis, z-axis respectively.
# with 0 ≤ θ ≤ 2π and 0 ≤ Φ ≤ 2π 



# Code:

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


theta = np.linspace(0, 2*np.pi, 50) 
phi = np.linspace(0, 2*np.pi, 50)


theta_grid, phi_grid = np.meshgrid(theta, phi) 

# R = 70 and r = 15
x_grid = (70 + 15 * np.cos(theta_grid)) * np.cos(phi_grid)

y_grid = (70 + 15 * np.cos(theta_grid)) * np.sin(phi_grid) 

z_grid = 15 * np.sin(theta_grid)

fig = plt.figure(figsize = (50,50))

ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x_grid, y_grid, z_grid, rstride = 2, cstride = 2, color = 'grey')

ax.set_xlim(-100,100)

ax.set_ylim(-100,100)

ax.set_zlim(-100,100)

plt.show()
