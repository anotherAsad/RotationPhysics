#! /usr/bin/python

# Rotation Mechanics
# (+a, +b) = (x+, y-) --> Convention

# Lacking a true modelling of force. Currently, only dependent on the distance from the centre,
# does not mind to keep the particle from falling into centre.
# More of a planetary model

# Note that acceleration is directly proportional to distance. Which is truly the case if omega is constant

import cv2
import numpy

def render():
	global pt1, pt2, screen, pathTuples
	screen = numpy.zeros((600, 800, 1), numpy.uint8)
	intPt1, intPt2 = (int(pt1[0]), int(pt1[1])) , ( int(pt2[0]), int(pt2[1]) )

	if len(pathTuples) > 50:
		pathTuples.pop(0)
	for x in pathTuples:
		cv2.circle(screen, x, 1, 63, -1)

	cv2.circle(screen, intPt1, 5, 255, -1)
	cv2.circle(screen, intPt2, 5, 255, -1)
	return

def update():
	global pt1, vel1, pathTuples
	pt1 = (pt1[0]+vel1[0]/5.0, pt1[1]+vel1[1]/5.0)
	pathTuples.append( (int(pt1[0]), int(pt1[1])) )
	distx = pt1[0] - pt2[0]
	disty = pt1[1] - pt2[1]
	# Application of a force proportional to distance that changes the velocity vectors
	vel1 = (vel1[0] - distx / 7.0 , vel1[1] - disty / 7.0)
	return

screen = numpy.zeros((600, 800, 1), numpy.uint8)
pt1 = (200, 320)
pt2 = (260, 320)
vel1 = (0, 20)
pathTuples = []

while cv2.waitKey(100) != 27:
	update()
	render()
	cv2.imshow('window', screen)
	print (vel1[0]**2 + vel1[1]**2)**0.5
cv2.waitKey(0)
