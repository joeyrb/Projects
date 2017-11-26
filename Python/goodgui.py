#!/usr/bin/python
from __future__ import print_function
import img_viewer as ImgViewer
from PIL import Image
from graphics import *

# GLOBALS
SIZE_X = 640
SIZE_Y = 640
WIN_CENTER = Point(SIZE_X/2, SIZE_Y/2)

# FUNCTIONS
def setWindow():
	win = GraphWin("GoodGui", SIZE_X,SIZE_Y)
	win.setBackground('black')
	win.setCoords(0,0, SIZE_X, SIZE_Y)
	return win

def setButton(win, p1, p2, bg_color, text):
	btn = Rectangle(p1, p2)
	btn.setFill(bg_color)
	btn.setOutline(bg_color)
	txt = Text(btn.getCenter(), text)
	txt.setSize(12)
	txt.setTextColor('black')
	btn.draw(win)
	txt.draw(win)
	return btn

def setPrevButton(win):
	p1 = Point(0,50)
	p2 = Point(100, 0)
	return setButton(win, p1, p2, 'lime', "< Prev")

def setNextButton(win):
	p1 = Point(SIZE_X, 50)
	p2 = Point(SIZE_X-100, 0)
	return setButton(win, p1, p2, 'lime', "Next >")

def getImages(path):
	return ImgViewer.loadImgs(path)

def displayImages(imgList):
	pass

# MAIN
def main():
	win = setWindow()
	prev_btn = setPrevButton(win)
	next_btn = setNextButton(win)
	win.getMouse()
	win.close()

if __name__ == '__main__':
	main()
