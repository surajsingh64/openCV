import cv2
cap =cv2.VideoCapture(0)
while True:
    ret,frame=cap.read() # ret is boolean value if frame is captured or not
    if not ret:
        print("failed to capture video")
        break
    cv2.imshow('Video Capture',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):# Press 'q' to close the video window
        print("video stopped by user")
        break

cap.release()
cv2.destroyAllWindows() 