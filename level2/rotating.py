import cv2
locationofimage = input("Enter the location of image eg img.png: ")
image = cv2.imread(locationofimage)
if image is not None:
    m=cv2.getRotationMatrix2D((image.shape[1]//2, image.shape[0]//2), 45, 1) # Rotate 45 degrees around the center
    rotated_image = cv2.warpAffine(image, m, (image.shape[1], image.shape[0]))
    cv2.imshow('Rotated Image', rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('rotated_image.png', rotated_image)
else:
    print("Error: Could not load image.")
    