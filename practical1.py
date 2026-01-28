import cv2
locationofimage=input("Enter the location of image eg img.png: ")
image = cv2.imread(locationofimage)
if image is not None:
    to_do=input("Enter 's' to show image, 'g' to convert to greyscale, 'd' to display dimensions: ")
    if to_do=='s':
        cv2.imshow('Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif to_do=='g':
        grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Greyscale Image', grey_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        to_do_save=input("Do you want to save the greyscale image? (y/n): ")
        if to_do_save.lower()=='y':
            save_location=input("Enter the location to save e.g., greyscale.png: ")
            cv2.imwrite(save_location, grey_image)
            print(f"Greyscale image saved successfully as '{save_location}'.")
    elif to_do=='d':
        h,w,c= image.shape
        print(f"Height: {h}, Width: {w}, Channels: {c}")
    else:
        print("Invalid option.")
else:
    print("Error: Could not load image.")
