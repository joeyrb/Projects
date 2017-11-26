#!/usr/bin/python
'''
Messing around with some GUI programming in python. Turtle is
a simple graphics drawing module that uses tkinter.

Tkinter:
https://docs.python.org/3/library/tkinter.html#tkinter-modules

Turtle:
https://docs.python.org/3/library/turtle.html#module-turtle
'''
try:
	# for Python2
	from Tkinter import *
except ImportError:
	# for Python3
	from tkinter import *


def hello(event):
	print("Single Click, Button-1")

def quit(event):
	print("Double Click, stopping...")
	import sys; sys.exit()

def motion(event):
	print("Mouse position: (%s, %s)" % (event.x, event.y))
	return

def getNext(event):
	print("Right Key Pressed = NEXT")

def getPrev(event):
	print("Left key pressed = PREVIOUS")

def leftKeyPress(event):
	getPrev(event)

def rightKeyPress(event):
	getNext(event)

def main():
	# Setup root window
	root = Tk()
	root.bind('<Left>', leftKeyPress)
	root.bind('<Right>', rightKeyPress)
	root.bind('<Motion>', motion)

	# Setup Frame
	frame = Frame(root, width=100, height=100)

	# Setup Buttons
	widget = Button(root, text='Mouse Clicks')
	widget.bind('<Button-1>', hello)
	widget.bind('<Double-1>', quit)

	next_btn = Button(root, text='NEXT>', fg='green')
	next_btn.bind('<Button-1>', getNext)

	prev_btn = Button(root, text = '<PREV', fg='blue')
	prev_btn.bind('<Button-1>', getPrev)
	
	# Pack everything
	widget.pack()
	next_btn.pack(side='right')
	prev_btn.pack(side='left')
	frame.pack()

	# Display window
	frame.mainloop()


if __name__ == '__main__':
	main()


# TURTLE TUTORIAL
# from turtle import *
# color('yellow', 'blue')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()
