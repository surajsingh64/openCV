import cv2
img = cv2.imread('level5\pikachu.jpg', cv2.IMREAD_GRAYSCALE)
thresolded = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
#cv2.threshold(image, threshold_value, max_value, thresholding_type)
cv2.imshow('Thresolded Image',thresolded[1])
cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()