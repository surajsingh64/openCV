import cv2
locationofimage = input("Enter the location of image eg img.png: ")
image = cv2.imread(locationofimage)
if image is not None:  
    blurred_image = cv2.GaussianBlur(image, (15, 15), 3)
    cv2.imshow('Original Image', image)
    cv2.imshow('Gaussian Blurred Image', blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('gaussian_blurred_image.png', blurred_image)