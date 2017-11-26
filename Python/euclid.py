#!/usr/bin/python3
'''
Name:			Joey Brown
Description:	Calculates the Euclidian distance between two given points.
Usage:			Accepts the x & y coordinates of two points as command line args.
				$> python3 euclid.py x1 y1 x2 y2
'''
from tkinter import *
from math import sqrt
from sys import argv

# Function that calculates the Euclidian distance.
def euclidDist(x1, y1, x2, y2):
	return sqrt( ( (x2-x1)**2 ) + ( (y2-y1)**2 ) )

def main():
	WIDTH = 320
	HEIGHT = 240

	root = Tk()
	root.title("Euclidian Distance")
	root.minsize(WIDTH, HEIGHT)

	var = StringVar()

	label = Label(root, textvariable = var)
	label.place(x=HEIGHT/2, y = WIDTH/2-50)

	var.set("Distance: " + str(euclidDist( float(argv[1]), float(argv[2]), float(argv[3]), float(argv[4]) ) ))

	# Uncomment this to display the graphical window with distance
	# root.mainloop()
	
	print(euclidDist( float(argv[1]), float(argv[2]), float(argv[3]), float(argv[4]) ) )

if __name__ == '__main__':
	main()