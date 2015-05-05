#!/user/bin/python
"""
H3C7P21 - Fractal Landscapes

Authors: Derek Stotz
Date: 5/3/2015
Course: Natural Computing
Prof: Dr. Jeff McGough
Usage:
	python3 Landscapes.py <Width> <NRC> <Theta>
	
	Theta is the maximum height/depth change.  NRC is the number of divisions. 10 4 10 are good input parameters.

"""

from math import *
from sys import *
from matplotlib import mpl, animation
from matplotlib import pyplot as plt
import numpy as np
from scipy import signal
from mpl_toolkits.mplot3d import Axes3D
from random import *

DELTA = []

def rmd(Landscape, x0, y0, x2, y2, T, nrc):
	x1 = ((x0 + x2) // 2)
	y1 = ((y0 + y2) // 2)
	Landscape[x1][y1] = .5 * (Landscape[x0][y0] + Landscape[x2][y2]) + DELTA[T] * (2 * random() - 1)
	if T < nrc:
		rmd(Landscape, x0, y0, x1, y1, T+1, nrc)
		rmd(Landscape, x0, y1, x1, y2, T+1, nrc)
		rmd(Landscape, x1, y1, x2, y2, T+1, nrc)
		rmd(Landscape, x1, y0, x2, y1, T+1, nrc)

if __name__=="__main__":
	
	Width = int(argv[1])
	NRC = int(argv[2])
	theta = float(argv[3])

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	x = y = np.arange(-Width/2, Width/2, 1)
	X, Y = np.meshgrid(x, y)
	arr = np.array([0 for x,y in zip(np.ravel(X), np.ravel(Y))])
	Landscape = arr.reshape(X.shape)

	# generate the landscape using a recursive midpoint displacement algorithm
	seed()
	Landscape[Width-1, Width-1] = theta * (2 * random() - 1)
	for i in range (0, NRC+1):
			DELTA.append(theta * .5**((i+1)/2))
	rmd(Landscape, 0, 0, Width-1, Width-1, 0, NRC)

	# display landscape
	ax.plot_surface(X, Y, Landscape)
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')

	mng = plt.get_current_fig_manager()
	mng.resize(*mng.window.maxsize())

	plt.show()
