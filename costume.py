import sys
from PIL import Image

Image = []

for arg in sys.argv:
    image = Image.open(arg)
    image.append(image)


images[0].save