import cv2
locationofimage = input("Enter the location of image eg img.png: ")
image = cv2.imread(locationofimage)
if image is not None:
    cropped_image = image[50:250, 50:250] , # Crop a 200x200 pixels region starting from (50,50)
    cv2.imshow('Cropped Image', cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('cropped_image.png', cropped_image)
else:
    print("Error: Could not load image.")

