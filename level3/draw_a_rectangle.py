import cv2
locationofimage = input("Enter the location of image eg img.png: ")
image = cv2.imread(locationofimage)
if image is not None:
   #outside rectangle
   pt1 = (50, 50)  
   pt2 = (618, 390)
#eyes_1 rectangles
   pt3 = (200, 100)
   pt4 = (250, 150)
#eyes_2 rectangles
   pt5 = (468, 100)
   pt6=(418, 150)
#mouth rectangle
   pt7 = (250, 300)
   pt8 = (418, 350  )

   color = (255, 0, 0)  # Blue color in BGR
   thickness = 2  # Thickness of the rectangle border
   fill=-1  # Fill the rectangle
   image_with_rectangle = cv2.rectangle(image.copy(), pt1, pt2, color, fill)
   image_with_rectangle = cv2.rectangle(image_with_rectangle, pt3, pt4, (0, 255, 0), thickness)
   image_with_rectangle = cv2.rectangle(image_with_rectangle, pt5, pt6, (0, 0, 255), thickness)
   image_with_rectangle = cv2.rectangle(image_with_rectangle, pt7, pt8, (0, 255, 255), thickness)
   cv2.imshow('Image with Rectangle', image_with_rectangle)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   cv2.imwrite('image_with_rectangle.png', image_with_rectangle)