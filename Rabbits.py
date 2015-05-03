#!/user/bin/python
"""
H3C58P3 - StarLogo Rabbits Simulation

Authors: Derek Stotz
Date: 5/3/2015
Course: Natural Computing
Prof: Dr. Jeff McGough
Usage:
	python3 Rabbits.py <number of rabbits> <hatch threshold> <grass growth rate (0 -1.0)> <starvation rate(0 - 1)> <maximum number of generations>

Setting the starvation rate to something very low (like .05) and setting the growth rate to something also very low (like .001) give a good example of a fluxuating population.  The default parameters give a fairly generic example
"""

from math import *
from sys import *
from matplotlib import mpl, pyplot, animation
import numpy as np
from scipy import signal
from random import *

NUMBER = 100
HATCH_THRESHOLD = 5
GRASS_RATE = .01
STARVE_RATE = .3
G_MAX = 1000

BUNNIES = []
NROWS = 100
NCOLS = 100
GRASS = np.random.randint(2, size=(NROWS,NCOLS)) #half grass on, half grass off

class bunny:
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.energy = 1 # so it doesn't die right off the bat
		self.dead = False

def generation(i):
	if i > G_MAX:
		return

	global BUNNIES

	# move the bunnies
	for b in BUNNIES:
		rmove = (b.row + randint(0,1)*2 - 1 + NROWS) % NROWS # wander aimlessly
		cmove = (b.col + randint(0,1)*2 - 1 + NCOLS) % NCOLS
		if GRASS[rmove, cmove] == 1: # om nom
			b.energy += 1

		# move out
		GRASS[b.row, b.col] = 0
		b.row = rmove
		b.col = cmove

		if b.energy > HATCH_THRESHOLD: # lay an egg!
			BUNNIES.append(bunny(b.row, b.col))

		b.energy -= STARVE_RATE # starve a little
		if b.energy < 0: # starve to death :(
			b.dead = True
		else:
			GRASS[b.row, b.col] = 2
	# create a new list of the not dead bunnies
	BUNNIES = [s for s in BUNNIES if not s.dead]

	# grow the grass
	for r in range(0, NROWS):
		for c in range(0, NCOLS):
			if GRASS[r,c] < 1 and random() < GRASS_RATE:
				GRASS[r,c] = 1
	pyplot.cla()
	pyplot.imshow(GRASS,interpolation='nearest', cmap = cmap,norm=norm)
	pyplot.draw()

if __name__=="__main__":
	
	# load the start state from args
	seed()

	if(len(argv)>5):
		G_MAX = int(argv[5])
	if(len(argv)>4):
		STARVE_RATE = float(argv[4])
	if(len(argv)>3):
		GRASS_RATE = float(argv[3])
	if(len(argv)>2):
		HATCH_THRESHOLD = int(argv[2])
	if(len(argv)>1):
		NUMBER = int(argv[1])

	# generate some bunnies
	for i in range(0, NUMBER):
		BUNNIES.append(bunny(randint(0, NROWS-1), randint(0, NCOLS-1)))

	# set up the visualization
	fig = pyplot.figure()
	cmap = mpl.colors.ListedColormap(['black','green', 'red'])
	bounds=[0,0, 1,1, 2, 2]
	norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
	mng = pyplot.get_current_fig_manager()
	mng.resize(*mng.window.maxsize())

	#begin the game loop
	pyplot.imshow(GRASS,interpolation='nearest', cmap = cmap,norm=norm)
	a = animation.FuncAnimation(fig, generation, repeat=True, interval=10)
	pyplot.show()
