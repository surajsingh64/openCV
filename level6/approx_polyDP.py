import cv2
img = cv2.imread('level6\hexa.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
for contour in contours:
    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    courner=len(approx)
    if courner==3:
        shape="Triangle"
    elif courner==4:
        shape="Rectangle"
    elif courner==5:
        shape="Pentagon"
    elif courner==6:
        shape="Hexagon"
    elif courner==7:
        shape="Heptagon"
    elif courner==8:
        shape="Octagon"
    else:
        shape="Circle"
    cv2.drawContours(img, [approx], 0, (255, 0, 0), 5)
    x,y,w,h=cv2.boundingRect(approx)
    cv2.putText(img,shape,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
cv2.imshow('Approx PolyDP', img)
# save the image
cv2.imwrite('level6/approx_polyDP_output.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()