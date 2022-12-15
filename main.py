import json
import math

grid = json.loads(open('grid.json').read())

from PIL import Image
from PIL import ImageColor

img_data = []
boundary_size = 6
height = width = 100 * boundary_size
count = 0

for cell in range(len(grid)):
    row = cell // boundary_size
    col = cell % boundary_size
    color = grid[cell]['Type']
    if color == 0:
        color = 'black'
    elif color == 1:
        color = 'white'
    elif color == 2:
        color = 'green'
    elif color == 3:
        color = 'blue'
    elif color == 4:
        color = 'yellow'
    elif color == 5:
        color = 'brown'
    color = ImageColor.getrgb(color)
    purple = ImageColor.getrgb('purple')
    grey = ImageColor.getrgb('grey')
    for i in range(100):
        for j in range(100):
            x = row * 100 + i
            y = col * 100 + j
            img_data.append((x, y, color))
for cell in range(len(grid)):
    row = cell // boundary_size
    col = cell % boundary_size
    if grid[cell]['Type'] != 0:
        for i in range(100):
            img_data.append((row * 100 + i, col * 100, grey))
            img_data.append((row * 100 + i, col * 100 + 100, grey))
            img_data.append((row * 100 + 100, col * 100 + i, grey))
            img_data.append((row * 100, col * 100 + i, grey))
        for direction in grid[cell]['AvailableDirections']:
            direction = direction['Direction']
            for i in range(20):
                for j in range(10):
                    if direction['Item1']!=0:
                        x=row*100+39*abs(direction['Item1'])+i
                        y=col*100+45-50*direction['Item1']+j
                        img_data.append((x, y, purple))
                    if direction['Item2']!=0:
                        x = row * 100 + 45 + 50 * direction['Item2'] + j
                        y = col * 100 + 39*abs(direction['Item2']) + i
                        img_data.append((x, y, purple))
        #if grid[cell]['North']:
        #    for i in range(20):
        #        for j in range(10):
        #            img_data.append((row * 100 + 39 + i, col * 100 - 5 + j, purple))
        #if grid[cell]['South']:
        #    for i in range(20):
        #        for j in range(10):
        #            img_data.append((row * 100 + 39 + i, col * 100 + 95 + j, purple))
        #if grid[cell]['East']:
        #    for i in range(20):
        #        for j in range(10):
        #            img_data.append((row * 100 + 95 + j, col * 100 + 39 + i, purple))
        #if grid[cell]['West']:
        #    for i in range(20):
        #        for j in range(10):
        #            img_data.append((row * 100 - 5 + j, col * 100 + 39 + i, purple))

background = (0, 0, 0, 255)
img = Image.new('RGB', (width + 1, height + 1), background)
pixels = img.load()

# Set the pixel Types from our data
for d in img_data:
    pixels[d[0], d[1]] = d[2]

img.save("image.png")
