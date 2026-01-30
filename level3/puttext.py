import cv2
locationofimage = input("Enter the location of image eg img.png: ")
image = cv2.imread(locationofimage)
if image is not None:
    # Text parameters
    text1 = "Hello, guys"
    org1 = (200, 100)  # Position for text1
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color1 = (0, 255, 0)  # Green color in BGR
    thickness1 = 2

    text2 = "thanks for watching"
    org2 = (180, 320)  # Position for text2
    color2 = (0, 0, 255)  # Red color in BGR
    thickness2 = 2

    # Put text on the image
    image_with_text = cv2.putText(image.copy(), text1, org1, font, font_scale, color1, thickness1, cv2.LINE_AA)
    image_with_text = cv2.putText(image_with_text, text2, org2, font, font_scale, color2, thickness2, cv2.LINE_AA)

    # Display the image with text
    cv2.imshow('Image with Text', image_with_text)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the image with text
    cv2.imwrite('image_with_text.png', image_with_text)