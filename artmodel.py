#! /usr/bin/python

# Rotation Mechanics
# (+a, +b) = (x+, y-) --> Convention

# Bad planetary model after the design of 'Original Earth Orbit.bas' from 2016
# Constant force in magnitude acts on the rotating object towards the direction of centre
import cv2
import numpy

def render():
	global pt1, pt2, screen, pathTuples
	screen = numpy.zeros((600, 800, 1), numpy.uint8)
	intPt1, intPt2 = (int(pt1[0]), int(pt1[1])) , ( int(pt2[0]), int(pt2[1]) )
	
	for x in pathTuples:
		cv2.circle(screen, x, 1, 63, -1)

	cv2.circle(screen, intPt1, 5, 127, -1)
	cv2.circle(screen, intPt2, 5, 255, -1)
	return

def update():
	global pt1, vel1, pathTuples
	pt1 = (pt1[0]+vel1[0]/5.0, pt1[1]+vel1[1]/5.0)
	pathTuples.append( (int(pt1[0]), int(pt1[1])) )
	distx = pt1[0] - pt2[0]
	disty = pt1[1] - pt2[1]
	mag = (distx**2 +disty**2)**0.5
	distx /= mag
	disty /= mag
	# Application of a force proportional to distance that changes the velocity vectors
	vel1 = (vel1[0] - distx / 7.0 , vel1[1] - disty / 7.0)
	return

screen = numpy.zeros((600, 800, 1), numpy.uint8)
pt1 = (210, 320)
pt2 = (260, 320)
vel1 = (0, 2.0*5.976783352)
pathTuples = []

while cv2.waitKey(1) != 27: 
	update()
	render()
	cv2.imshow('window', screen)
	print (vel1[0]**2 + vel1[1]**2)**0.5
cv2.waitKey(0)
