from PIL import Image
import numpy as np

# Load the original image
original_img = Image.open('C:/Users/vishnu jangid/Desktop/dataset/Machinary.jpg')

# Define a list of transformations
transformations = [
    lambda img: img.rotate(40),               # Rotation
    lambda img: img.transpose(Image.FLIP_LEFT_RIGHT),  # Horizontal Flip
    lambda img: img.transpose(Image.FLIP_TOP_BOTTOM),  # Vertical Flip
    lambda img: img.transpose(Image.ROTATE_90),       # Rotation 90 degrees
    lambda img: img.transpose(Image.ROTATE_270),      # Rotation 270 degrees
    lambda img: img.transpose(Image.TRANSPOSE),       # Transpose
]

# Initialize a counter for generated images
num_generated_images = 0

# Apply transformations and save augmented images
for transform in transformations:
    # Apply each transformation multiple times
    for _ in range(10):  # You can adjust the number of times you want to apply each transformation
        augmented_img = transform(original_img)
        augmented_img.save(f'C:/Users/vishnu jangid/Desktop/dataset/vj/augmented_{num_generated_images}.jpg', 'JPEG')
        num_generated_images += 1

        # Break the loop when you have generated at least 40 images
        if num_generated_images >= 40:
            break

    if num_generated_images >= 40:
        break
