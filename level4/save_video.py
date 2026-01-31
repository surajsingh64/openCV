import cv2
cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
frame_width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 codec
out = cv2.VideoWriter('output.mp4', fourcc, 90.0, (frame_width, frame_height))
while True:
    success, frame = cap.read()  # ret is boolean value if frame is captured or not
    if not success:
        print("failed to capture video")
        break
    out.write(frame)  # Write the frame to the output file
    cv2.imshow('Video Capture', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to close the video window
        print("video stopped by user")
        break
cap.release()
out.release()
cv2.destroyAllWindows()
