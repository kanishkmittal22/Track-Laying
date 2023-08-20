# # Maroon 5 - Maps

# from PIL import Image

# img = Image.open("map.jpeg")

# width, height = img.size
# matrix = [[None] * width for _ in range(height)]

# for x in range(width):
#     for y in range(height):
#         r, g, b = img.getpixel((x, y))
#         if max(r,g,b) == g and g>100:   # Green (grassy area)
#             matrix[y][x] = "G"
#         elif r == 152 and g == 83 and b == 26:   # Brown (mountains)
#             matrix[y][x] = "M"
#         elif max(r,g,b) == b and b>100:   # Blue (water bodies)
#             matrix[y][x] = "W"
#         else:
#             matrix[y][x] = "X"

# # Print the matrix
# for row in matrix:
#     for boi in row:
#         print(boi, end='')
#     print()


from PIL import Image

img = Image.open("mapss.jpeg")

width, height = img.size
matrix = [[None] * width for _ in range(height)]

for x in range(width):
    for y in range(height):
        r, g, b = img.getpixel((x, y))
        if max(r,g,b) == g and g>100:   # Green (grassy area)
            matrix[y][x] = "*"
        elif r == 152 and g == 83 and b == 26:   # Brown (mountains)
            matrix[y][x] = "M"
        elif max(r,g,b) == b and b>100:   # Blue (water bodies)
            matrix[y][x] = "W"
        else:
            matrix[y][x] = "X"

# Write the matrix to a file
with open("kanishkjob.txt", "w") as f:
    for row in matrix:
        for boi in row:
            f.write(boi)
        f.write('\n')
