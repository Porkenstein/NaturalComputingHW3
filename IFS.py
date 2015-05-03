#!/user/bin/python
"""
H3C7P15 - RIFS

Authors: Derek Stotz
Date: 5/3/2015
Course: Natural Computing
Prof: Dr. Jeff McGough
Usage:
	python3 IFS.py <fractal filename> <max iterations>
	
	Implement a RIFS to generate all the fractals whose codes are presented in Table 7.3
"""

import turtle
from math import *
from sys import *
from random import *

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# t is the turtle. Other letters are the relevant IFS code values
def draw_option(t, a, b, c, d, e, f):
	

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
	flag = False # after the flag is raised, done with first line
	for line in fin:
		sline = line.split(' ')
		if not flag:
			flag = True
			x = int(sline[0])
			y = int(sline[1])
		else:
			a.append(float(sline[0]))
			b.append(float(sline[1]))
			c.append(float(sline[2]))
			d.append(float(sline[3]))
			e.append(float(sline[4]))
			f.append(float(sline[5]))
			p.append(float(sline[6]))

	#begin drawing the fractal
	wn = turtle.Screen()
	t = turtle.Turtle()
	t.ht()

	for i in range(0, max_iter):
		j = 0
		roulette = random()
		for k in range(0, len(p)):
			roulette -= p[k]
			if roulette <= 0:
				j = k
		#tcor = [t.xcor(), t.ycor()]	
		draw_option(t, a[j], b[j], c[j], d[j], e[j], f[j])
