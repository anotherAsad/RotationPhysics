#! /usr/bin/python

# Rotation Mechanics
# (+a, +b) = (x+, y-) --> Convention

import cv2
import numpy

def render():
	global pt1, pt2, screen
	screen = numpy.zeros((600, 800, 1), numpy.uint8)
	intPt1, intPt2 = (int(pt1[0]), int(pt1[1])) , ( int(pt2[0]), int(pt2[1]) )
	cv2.circle(screen, intPt1, 5, 255, -1)
	cv2.circle(screen, intPt2, 5, 255, -1)
	return

def update():
	global pt1, pt2, vel1
	pt1 = (pt1[0]+vel1[0]/12.0, pt1[1]+vel1[1]/12.0)
	# Original length of the bond is 20

	# Magintude of distance b/w particles
	dist = ( (pt1[0] - pt2[0])**2 +  (pt1[1] - pt2[1])**2    )**0.5
	# to subtract the original distance from the extended length, we need to scale the x and y down
	curtailFactor = dist / 20.0
	distx = (pt1[0]-pt2[0]) - (pt1[0]-pt2[0])/curtailFactor
	disty = (pt1[1]-pt2[1]) - (pt1[1]-pt2[1])/curtailFactor
	
	# Application of force to change the velocity vector
	vel1 = (vel1[0] - 3*distx , vel1[1] - 3*disty)
	return

screen = numpy.zeros((600, 800, 1), numpy.uint8)
pt1 = (240, 320)
pt2 = (260, 320)
vel1 = (0, 30)

while cv2.waitKey(100) != 27:
	update()
	render()
	cv2.imshow('window', screen)
	print (vel1[0]**2 + vel1[1]**2)**0.5,
	print "\t\t",
	print ( (pt1[0] - pt2[0])**2 +  (pt1[1] - pt2[1])**2  )**0.5
cv2.waitKey(0)
