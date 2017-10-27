from PIL import Image

# Open image from hardcoded string
# im = Image.open("2/322_1000.jpg")
# im.show()

# Open image from raw_input string
# im = raw_input("img filepath: ")
# img = Image.open(im)

with open("images.txt") as f:
	s = f.readlines()
s = [x.strip() for x in s]
for lines in s:
	# print(lines)
	img = Image.open("2/" + lines.strip("\n"))
	img.show()
# im = Image.open(StringIO.StringIO(s))

# Display Image
# img.show()

