#! /usr/bin/python

# Rotation Mechanics
# (+a, +b) = (x+, y-) --> Convention

# Diparticle Molecule Model

import cv2
import numpy

def render():
	global pt1, pt2, screen, PathTuples
	screen = numpy.zeros((600, 800, 1), numpy.uint8)
	intPt1, intPt2 = (int(pt1[0]), int(pt1[1])) , ( int(pt2[0]), int(pt2[1]) )
	for x in PathTuples:
		cv2.circle(screen, x, 2 ,127, -1)
	cv2.circle(screen, intPt1, 5, 255, -1)
	cv2.circle(screen, intPt2, 5, 255, -1)

	return

def update():
	global pt1, pt2, vel1, vel2, PathTuples
	pt1 = (pt1[0]+vel1[0]/12.0, pt1[1]+vel1[1]/12.0)
	pt2 = (pt2[0]+vel2[0]/12.0, pt2[1]+vel2[1]/12.0)
	# Original length of the bond is 20

	# Magintude of distance b/w particles
	dist = ( (pt1[0] - pt2[0])**2 +  (pt1[1] - pt2[1])**2    )**0.5
	# to subtract the original distance from the extended length, we need to scale the x and y down
	curtailFactor = dist / 20.0
	distx = (pt1[0]-pt2[0]) - (pt1[0]-pt2[0])/curtailFactor
	disty = (pt1[1]-pt2[1]) - (pt1[1]-pt2[1])/curtailFactor
	
	# Application of force to change the velocity vector
	vel1 = (vel1[0] - 2.0*distx , vel1[1] - 2.0*disty)
	vel2 = (vel2[0] + 2.0*distx , vel2[1] + 2.0*disty)

	# Register Path
	PathTuples.append( ( int((pt1[0]+pt2[0])/2.0) , int((pt1[1]+pt2[1])/2.0) )  )
	return

screen = numpy.zeros((600, 800, 1), numpy.uint8)
PathTuples = []
pt1 = (240, 120)
pt2 = (260, 120)
vel1 = (30, 0)
vel2 = (-30, 0)

while cv2.waitKey(100) != 27:
	update()
	render()
	cv2.imshow('window', screen)
	print (vel1[0]**2 + vel1[1]**2)**0.5, "\t\t",
	print (vel2[0]**2 + vel2[1]**2)**0.5, "\t\t",
	print (vel1[0]**2 + vel1[1]**2)**0.5 + (vel2[0]**2 + vel2[1]**2)**0.5, "\t\t"
	print ( (pt1[0] - pt2[0])**2 +  (pt1[1] - pt2[1])**2  )**0.5, "\n"
cv2.waitKey(0)
