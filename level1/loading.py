# Import OpenCV library for image processing
import cv2

# Load image from file
image = cv2.imread('doctor.png')

# Check if image was loaded successfully
if image is None:
    print("Error: Could not load image.")
else:   
    # Display the image in a window
    cv2.imshow('Loaded Image', image)
    # Wait for key press (0 means wait indefinitely)
    cv2.waitKey(0)
    # Close all windows
    cv2.destroyAllWindows()
    print("Image loaded successfully.")

# Save the processed image to a file
cv2.imwrite('saved_image.png', image)

print("Image saved successfully as 'saved_image.png'.") 