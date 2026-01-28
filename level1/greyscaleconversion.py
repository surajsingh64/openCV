import cv2
image = cv2.imread('doctor.png')
if image is not None:
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Greyscale Image', grey_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()