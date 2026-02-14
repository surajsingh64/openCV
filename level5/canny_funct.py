import cv2
img=cv2.imread("level5/pikachu.jpg",cv2.IMREAD_GRAYSCALE)
edges=cv2.Canny(img,50,200)
cv2.imshow("Canny Edges",edges)
cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()