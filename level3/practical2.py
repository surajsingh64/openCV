import cv2
locationofimage = input("Enter the location of image eg img.png: ")
image = cv2.imread(locationofimage)
if image is not None:
    #making all thing togher by asking user for draw shape( circle,rectangle,line, text
    while True:
        shape = input("Enter the shape (circle/rectangle/line/text) or 'done' to finish: ").lower()
        if shape == "done":
            break
        if shape == "circle":
            # Take center point and radius from user
            center_x = int(input("Enter the x of circle: "))
            center_y = int(input("Enter the y of circle: "))
            radius = int(input("Enter the radius of circle: "))
            color = (0, 255, 0)  # Green color in BGR
            thickness = int(input("Enter the thickness of circle: "))
            center_point = (center_x, center_y)
            image = cv2.circle(image, center_point, radius, color, thickness)
        elif shape == "rectangle":
            # Take top-left and bottom-right points from user
            x1 = int(input("Enter the x1 of rectangle: "))
            y1 = int(input("Enter the y1 of rectangle: "))
            x2 = int(input("Enter the x2 of rectangle: "))
            y2 = int(input("Enter the y2 of rectangle: "))
            color = (255, 0, 0)  # Blue color in BGR
            thickness = int(input("Enter the thickness of rectangle: "))
            pt1 = (x1, y1)
            pt2 = (x2, y2)
            image = cv2.rectangle(image, pt1, pt2, color, thickness)
        elif shape == "line":
            # Take start and end points from user
            x1 = int(input("Enter the x1 of line: "))
            y1 = int(input("Enter the y1 of line: "))
            x2 = int(input("Enter the x2 of line: "))
            y2 = int(input("Enter the y2 of line: "))
            color = (255, 255, 0)  # Cyan color in BGR
            thickness = int(input("Enter the thickness of line: "))
            pt1 = (x1, y1)
            pt2 = (x2, y2)
            image = cv2.line(image, pt1, pt2, color, thickness)
        elif shape == "text":
            # Take text and position from user
            text = input("Enter the text to put on image: ")
            x = int(input("Enter the x position for text: "))
            y = int(input("Enter the y position for text: "))
            org = (x, y)
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            color = (0, 0, 255)  # Red color in BGR
            thickness = 2
            image = cv2.putText(image, text, org, font, font_scale, color, thickness, cv2.LINE_AA)
        else:
            print("invalid shape!")
    # Display the image after each shape is added
    cv2.imshow('Final Modified Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Save the image
    cv2.imwrite('modified_image.png', image)
    