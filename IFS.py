#!/user/bin/python
"""
H3C7P15 - RIFS

Authors: Derek Stotz
Date: 5/3/2015
Course: Natural Computing
Prof: Dr. Jeff McGough
Usage:
	python3 IFS.py <fractal filename> <max iterations>
	
	Implementation of an a RIFS to generate all the fractals whose codes are presented in Table 7.3.
	between 100000 and 1000000 iterations and a starting point of 0 0 are reccomended.  Point Size depends on the fractal. The latter two are defined on the first line of the input file.
"""

import numpy as np
from math import *
from sys import *
from random import *
import matplotlib.pyplot as plt
from numpy.random import rand

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# letters are the relevant IFS code values, point is the point to transform
# see page 605 in the text for a guide
def aff_transform(point, a, b, c, d, e, f):
	A = np.array([[a, b],[c, d]])
	t = np.array([[e],[f]])
	return (np.dot(A, point) + t)
	pass

if __name__=="__main__":

	fin = open(argv[1])
	max_iter = int(argv[2])
	a = []
	b = []
	c = []
	d = []
	e = []
	f = []
	p = []
	x = []
	y = []
	flag = False # after the flag is raised, done with first line
	for line in fin:
		sline = line.split(' ')
		if not flag:
			flag = True
			x.append(float(sline[0]))
			y.append(float(sline[1]))
			pointsize = float(sline[2])
		else:
			a.append(float(sline[0]))
			b.append(float(sline[1]))
			c.append(float(sline[2]))
			d.append(float(sline[3]))
			e.append(float(sline[4]))
			f.append(float(sline[5]))
			p.append(float(sline[6]))

	# generate the fractal
	# let the user know that something is happening
	print("Building " + str(argv[1]) + " at " + str(max_iter) + " iterations...   0%", end="")

	point = np.array([[x[0]],[y[0]]])
	i = 0
	for i in range(0, max_iter):
		#progress elipses
		if max_iter > 100 and i % (max_iter//100) is 0:
			for m in range(0, len(str(int(i / max_iter * 100)) + '%')):
				print('\b', end="")
			print(str(int(i / max_iter * 100)) + '%', end="")
			stdout.flush()
		j = 0
		roulette = random()
		for k in range(0, len(p)):
			roulette -= p[k]
			if roulette <= 0:
				j = k
				break
		new_point = aff_transform(point, a[j], b[j], c[j], d[j], e[j], f[j])
		x.append(new_point[0][0])
		y.append(new_point[1][0])
		point = new_point

	for m in range(0, len(str(int(i / max_iter * 100)) + '%')):
		print('\b', end="")
	print('100%', end="")
	print('\n')

	print('Drawing Fractal...')
	stdout.flush()

	#begin drawing the fractal
	plt.grid(True)
	plt.scatter(x,y, s = pointsize)
	mng = plt.get_current_fig_manager()
	mng.resize(*mng.window.maxsize())

	ax = plt.subplot(111)
	maxdim = max(ax.get_xlim()[1], ax.get_ylim()[1])
	mindim = min(ax.get_xlim()[0], ax.get_ylim()[0])
	ax.set_xlim(mindim, maxdim)
	ax.set_ylim(mindim, maxdim)

	plt.show()
