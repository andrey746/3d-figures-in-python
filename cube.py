from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# vertices of a pyramid
v = np.array([[-1, -1, -1], [1, -1, -1], [1, 1, -1],  [-1, 1, -1], [-1, -1, 1], [1, -1, 1], [1, 1, 1],  [-1, 1, 1] ])
ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])


# generate list of sides' polygons of our pyramid
verts = [ [v[0],v[1],v[2], v[3]], [v[0],v[4],v[5],v[1]],
 [v[1],v[5],v[6],v[2]], [v[2],v[6],v[7],v[3]], [v[3],v[7],v[4],v[0]], [v[4],v[7],v[6],v[5]]  ]

# plot sides
ax.add_collection3d(Poly3DCollection(verts, facecolors='orange', linewidths=0.8, edgecolors='black', alpha=.25))


 
plt.show()