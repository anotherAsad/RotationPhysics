#! /usr/bin/python

# Rotation Mechanics
# (+a, +b) = (x+, y-) --> Convention

# Diparticle Molecule Model

import cv2
import numpy

def render():
	global pt1, pt2, pt3, pt4, pt5, screen, PathTuples
	screen = numpy.zeros((600, 800, 1), numpy.uint8)
	intPt1 = ( int(pt1[0]), int(pt1[1]) )
	intPt2 = ( int(pt2[0]), int(pt2[1]) )
	intPt3 = ( int(pt3[0]), int(pt3[1]) )
	intPt4 = ( int(pt4[0]), int(pt4[1]) )
	intPt5 = ( int(pt5[0]), int(pt5[1]) )

	for x in PathTuples:
		cv2.circle(screen, x, 2 , 64, -1)
	cv2.circle(screen, intPt1, 5, 255, -1)
	cv2.circle(screen, intPt2, 5, 127, -1)
	cv2.circle(screen, intPt3, 5, 190, -1)
	cv2.circle(screen, intPt4, 5, 127, -1)
	cv2.circle(screen, intPt5, 5, 255, -1)

	return

def applyForce(ptA, ptB, velA, velB, orgDist):
	# Magintude of distance b/w particles
	dist = ( (ptA[0] - ptB[0])**2 +  (ptA[1] - ptB[1])**2    )**0.5
	# To subtract the original distance from the extended length, we need to scale the x and y down
	curtailFactor = dist / orgDist
	distx = (ptA[0]-ptB[0]) - (ptA[0]-ptB[0])/curtailFactor
	disty = (ptA[1]-ptB[1]) - (ptA[1]-ptB[1])/curtailFactor
	# Application of force to change the velocity vector
	velA = (velA[0] - 8.0*distx , velA[1] - 8.0*disty)
	velB = (velB[0] + 8.0*distx , velB[1] + 8.0*disty)
	return velA, velB

def update():
	global pt1, pt2, pt3, pt4, pt5, vel1, vel2, vel3, vel4, vel5, PathTuples
	pt1 = (pt1[0]+vel1[0]/12.0, pt1[1]+vel1[1]/12.0)
	pt2 = (pt2[0]+vel2[0]/12.0, pt2[1]+vel2[1]/12.0)
	pt3 = (pt3[0]+vel3[0]/12.0, pt3[1]+vel3[1]/12.0)
	pt4 = (pt4[0]+vel4[0]/12.0, pt4[1]+vel4[1]/12.0)
	pt5 = (pt5[0]+vel5[0]/12.0, pt5[1]+vel5[1]/12.0)

	vel1, vel2 = applyForce(pt1, pt2, vel1, vel2, 20.0)
	vel2, vel3 = applyForce(pt2, pt3, vel2, vel3, 20.0)
	vel3, vel4 = applyForce(pt3, pt4, vel3, vel4, 20.0)
	vel4, vel5 = applyForce(pt4, pt5, vel4, vel5, 20.0)
	
	vel1, vel3 = applyForce(pt1, pt3, vel1, vel3, 40.0)
	vel1, vel4 = applyForce(pt1, pt4, vel1, vel4, 60.0)
	vel1, vel5 = applyForce(pt1, pt5, vel1, vel5, 80.0)

	vel2, vel4 = applyForce(pt2, pt4, vel2, vel4, 40.0)
	vel2, vel5 = applyForce(pt2, pt5, vel2, vel5, 60.0)

	vel3, vel5 = applyForce(pt3, pt5, vel3, vel5, 40.0) 
	# Register Path
	PathTuples.append( ( int((pt1[0]+pt2[0]+pt3[0]+pt4[0]+pt5[0])/5.0) , int((pt1[1]+pt2[1]+pt3[1]+pt4[1]+pt5[1])/5.0) )  )
	return

screen = numpy.zeros((600, 800, 1), numpy.uint8)
PathTuples = []
pt1 = (240, 120)
pt2 = (260, 120)
pt3 = (280, 120)
pt4 = (300, 120)
pt5 = (320, 120)

vel1 = (0, 30)
vel2 = (0, 00)
vel3 = (0, 00)
vel4 = (0, 60)
vel5 = (0, 00)

while cv2.waitKey(100) != 27:
	print (vel1[0]**2 + vel1[1]**2)**0.5, "\t",
	print (vel2[0]**2 + vel2[1]**2)**0.5, "\t",
	print (vel3[0]**2 + vel3[1]**2)**0.5, "\t",
	print (vel4[0]**2 + vel4[1]**2)**0.5, "\t",
	print (vel5[0]**2 + vel5[1]**2)**0.5, "\t",
	print "\n\n"
	render()
	update()
	cv2.imshow("window", screen)

cv2.waitKey(0)
