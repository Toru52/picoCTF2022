import numpy as np
from PIL import Image

# Open images
print("ok")
im1 = Image.open("scrambled1.png")
im2 = Image.open("scrambled2.png")

# Make into Numpy arrays
im1np = np.array(im1)
im2np = np.array(im2)

# Add images
result = im2np + im1np
# Convert back to PIL image and save
Image.fromarray(result).save('result.png')