#  -------------------------------------  Parametric Surface Plotting of an Ellipsoid  -----------------------------------------


# The parametric equation of an Ellipsoid is (a cosθ sinΦ)i + (b sin⁡θ sinΦ)j + (c cos⁡Φ)k where a,b,c > 0 
# a,b,c are the radius in each component and i,j,k being unit vectors in the direction of x-axis, y-axis, z-axis respectively.
# with 0 ≤ θ ≤ 2π and 0 ≤ Φ ≤ π

# These parameters may be interpreted as spherical coordinates, where θ is the polar angle 
# and Φ is the azimuth angle of the point (x, y, z) of the ellipsoid.


# Code:

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


theta = np.linspace(0, 2*np.pi, 50) 
phi = np.linspace(0, np.pi, 50)

theta_grid, phi_grid = np.meshgrid(theta, phi) 

x_grid = 6 * np.cos(theta_grid) * np.sin(phi_grid) # taking a = 6

y_grid = 3 * np.sin(phi_grid) * np.sin(theta_grid) # taking b = 3

z_grid = 2 * np.cos(phi_grid) # taking c = 2

fig = plt.figure(figsize = (15,15))

ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x_grid, y_grid, z_grid, rstride = 2, cstride = 2, color = 'green')

plt.show()
