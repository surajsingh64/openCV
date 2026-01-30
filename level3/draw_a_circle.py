import cv2
locationofimage = input("Enter the location of image eg img.png: ")
image = cv2.imread(locationofimage) 
if image is not None:
    #outside circle
    center_coordinates = (334, 220)  
    radius = 170
    #eyes_1 circle
    center_coordinates1 = (250, 150)
    radius1 = 25
    #eyes_2 circle
    center_coordinates2 = (418, 150)
    radius2 = 25
    #mouth circle
    center_coordinates3 = (334, 320)
    radius3 = 50
    
    color = (255, 0, 0)  # Blue color in BGR
    thickness = 2  # Thickness of the circle border
    fill=-1  # Fill the circle
    image_with_circle = cv2.circle(image.copy(), center_coordinates, radius, color, fill)
    image_with_circle = cv2.circle(image_with_circle, center_coordinates1, radius1, (0, 255, 0), thickness)
    image_with_circle = cv2.circle(image_with_circle, center_coordinates2, radius2, (0, 0, 255), thickness)
    image_with_circle = cv2.circle(image_with_circle, center_coordinates3, radius3, (0, 255, 255), thickness)
    cv2.imshow('Image with Circle', image_with_circle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('image_with_circle.png', image_with_circle)