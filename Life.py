#!/user/bin/python
"""
H3C58P4 - Conway's Game of Life

Authors: Derek Stotz
Date: 5/3/2015
Course: Natural Computing
Prof: Dr. Jeff McGough
Usage:
	python3 Life.py <starting configuration file> <generations per second> <maximum number of generations>

	The starting configuration file is structued so the first line has the height and width of the playing field
	Subsequent lines are rows in the playing field.  0s are cells which are dead, and 1s are cells which are alive.
"""

from math import *
from sys import *
from matplotlib import mpl, pyplot, animation
import numpy as np
from scipy import signal

S = None
G_MAX = -1
NROWS = -1
NCOLS = -1
NEIGHBORHOOD_MASK = np.ones((3,3))
NEIGHBORHOOD_MASK[1,1] = 0 # discount the cell itself in its neighborhood

def generation(i):
	if i > G_MAX:
		return	

	# convolve S with a 3x3 to get a neighborhood matrix
	N = signal.convolve2d(S, NEIGHBORHOOD_MASK, boundary='wrap',mode='same')

	for r in range(0, NROWS):
		for c in range(0, NCOLS):
			if N[r][c] > 3:
				S[r,c] = 0
				continue
			if N[r][c] > 2:
				S[r,c] = 1
				continue
			if N[r][c] < 2:
				S[r,c] = 0
	pyplot.cla()
	pyplot.imshow(S,interpolation='nearest', cmap = cmap,norm=norm)
	pyplot.draw()

if __name__=="__main__":
	
	# load the start state from a file
	fin = open(argv[1])
	row = 0
	for line in fin:
		if row is 0:
			NROWS = int(line.split(' ')[0])
			NCOLS = int(line.split(' ')[1])
			S = np.zeros((NROWS, NCOLS))
		else:
			for i in range(0, NCOLS):
				if line[i] != '0':
					S[row,i] = 1
		if row is NROWS:
			break
		row +=1

	# set up the visualization
	fig = pyplot.figure()
	cmap = mpl.colors.ListedColormap(['white','black'])
	bounds=[0,0, 1,1]
	norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
	mng = pyplot.get_current_fig_manager()
	mng.resize(*mng.window.maxsize())

	#begin the game loop
	pyplot.imshow(S,interpolation='nearest', cmap = cmap,norm=norm)
	G_MAX = int(argv[2])
	a = animation.FuncAnimation(fig, generation, repeat=True, interval=10)
	pyplot.show()
