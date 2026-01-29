import cv2
locationofimage = input("Enter the location of image eg img.png: ")
image = cv2.imread(locationofimage)
if image is not None:
    resized_image = cv2.resize(image, (200, 200)) # Resize to 200x200 pixels width x height
    cv2.imshow('Resized Image', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('resized_image.png', resized_image) 
else:
    print("Error: Could not load image.")

