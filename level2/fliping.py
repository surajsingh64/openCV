import cv2
locationofimage = input("Enter the location of image eg img.png: ")
image = cv2.imread(locationofimage) 
if image is not None:
    flipped_horizontal = cv2.flip(image, 1)  # Flip the image horizontally
    flipped_vertical = cv2.flip(image, 0)  # Flip the image vertically
    cv2.imshow('Original Image', image)
    cv2.imshow('Flipped Horizontally', flipped_horizontal)
    cv2.imshow('Flipped Vertically', flipped_vertical)
    cv2.waitKey(0)
    cv2.destroyAllWindows()