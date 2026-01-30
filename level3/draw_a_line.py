import cv2
locationofimage = input("Enter the location of image eg img.png: ")
image = cv2.imread(locationofimage)
if image is not None:
    # Frame border coordinates for image dimensions (Height: 440, Width: 686)
    # Top-left to bottom-left (left vertical line)
    start_point_1 = (20, 20)
    end_point_1 = (20, 420)
    
    # Top-left to top-right (top horizontal line)
    start_point_2 = (20, 20)
    end_point_2 = (666, 20)
    
    # Top-right to bottom-right (right vertical line)
    start_point_3 = (666, 20)
    end_point_3 = (666, 420)
    
    # Bottom-left to bottom-right (bottom horizontal line)
    start_point_4 = (20, 420)
    end_point_4 = (666, 420)

    color = (0, 255, 0)  # Green color in BGR
    thickness = 2  # Thickness of the line

    image_with_line = cv2.line(image.copy(), start_point_1, end_point_1, color, thickness)
    image_with_line = cv2.line(image_with_line, start_point_2, end_point_2, color, thickness)
    image_with_line = cv2.line(image_with_line, start_point_3, end_point_3, color, thickness)
    image_with_line = cv2.line(image_with_line, start_point_4, end_point_4, color, thickness)

    cv2.imshow('Image with Line', image_with_line)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cv2.imwrite('image_with_line.png', image_with_line)