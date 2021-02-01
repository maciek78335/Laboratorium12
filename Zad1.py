### Pokazanie czajnika w 3D

!pip install tensorflow-graphics
!pip install trimesh

import numpy as np
import tensorflow as tf
import trimesh

import tensorflow_graphics.geometry.transformation as tfg_transformation
from tensorflow_graphics.notebooks import threejs_visualization

!wget -N https://people.sc.fsu.edu/~jburkardt/data/obj/teapot.obj
# Load the mesh.
mesh = trimesh.load("teapot.obj")
mesh.show()
