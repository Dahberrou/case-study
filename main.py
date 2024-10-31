import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate and display histogram
def plot_histogram(image, title):
    plt.figure(figsize=(10, 5))
    plt.hist(image.ravel(), bins=256, range=[0, 256], color='gray')
    plt.title(title)
    plt.xlim([0, 256])
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.show()

# Step 1: Read the original image
original_image = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

# Step 2: Calculate and display the histogram of the original image
plot_histogram(original_image, 'Histogram of Original Image')

# Step 3: Perform histogram equalization
equalized_image = cv2.equalizeHist(original_image)

# Step 4: Calculate and display the histogram of the equalized image
plot_histogram(equalized_image, 'Histogram of Equalized Image')

# Step 5: Compare the original and equalized images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.show()
 