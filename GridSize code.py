from PIL import Image
import numpy as np # numpy, useful for assignement

# Load  image
image = Image.open("/mnt/data/MAP mtmoon.png").convert("RGB")

#Change size
grid_size = (30, 30)  # number of tiles
tile_width = image.width // grid_size[1]
tile_height = image.height // grid_size[0]

# Initialize
grid = []

# Check tiles
for row in range(grid_size[0]):
    grid_row = []
    for col in range(grid_size[1]):
        # Get the tile's pixel data
        left = col * tile_width
        upper = row * tile_height
        right = left + tile_width
        lower = upper + tile_height
        tile = image.crop((left, upper, right, lower))

        # colour
        avg_color = np.array(tile).mean(axis=(0, 1))

        if is_wall(avg_color):  # walls
            grid_row.append(1)
        elif is_ladder(avg_color):  # ladders
            grid_row.append(2)
        else:
            grid_row.append(0)
    grid.append(grid_row)

# color represents a wall
def is_wall(color):
    return color[0] < 100 and color[1] < 100 and color[2] < 100  # Example for dark areas

# Fcolor represents a ladder
def is_ladder(color):
    return color[0] > 50 and color[2] > 150  # Example for blue areas

# Print/save 
for row in grid:
    print(row)
