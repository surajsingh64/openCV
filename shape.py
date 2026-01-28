import cv2
image= cv2.imread('doctor.png')
if image is not None:
    h,w,c= image.shape
    print(f"Height: {h}, Width: {w}, Channels: {c}")
else:
    print("Error: Could not load image.")