from __future__ import print_function
from PIL import Image

# Open image from hardcoded string
# im = Image.open("2/322_1000.jpg")
# im.show()

# Open image from raw_input string
# im = raw_input("img filepath: ")
# img = Image.open(im)
def main():
	with open("images.txt") as f:
		s = f.readlines()
	s = [x.strip() for x in s]
	for lines in s:
		# print(lines)
		img = Image.open("2/" + lines.strip("\n"))
		img.show()
		print("img =", img.mode, img.size)
# im = Image.open(StringIO.StringIO(s))

# Display Image
# img.show()

if __name__ == '__main__':
	main()