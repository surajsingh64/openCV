""" contour is a curve joining all the continuous points along the boundary which have same color or intensity.
It is useful for shape analysis, object detection and recognition.
hierarchy is the relationship between contours. It describes the parent-child relationship between contours. It is useful for contour retrieval mode.
cv2.findContours() is a function in OpenCV that is used to find contours in an image. It takes three arguments: the source image, the contour retrieval mode, and the contour approximation method. The function returns a list of contours and a hierarchy of contours.
cv2.findContours(image, mode, method) 
where image is the source image, -> binary image (usually obtained by thresholding or edge detection)
mode is the contour retrieval mode ->retrieval mode _> tell how many  and what kind of contours we want to find and how they are organized. 
method is the contour approximation method.-> contour approximation method is the method used to approximate the contour.

"""
import cv2
img = cv2.imread('level6/eagle.jpg')
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(grey,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)           
cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.imshow('Contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

