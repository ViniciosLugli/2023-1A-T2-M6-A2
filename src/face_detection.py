import cv2

# Load the classifier from the file: https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Read the input video
video_capture = cv2.VideoCapture('assets/input_demo.mp4')
# Nicola viciado em futebol kkkkkk

if not video_capture.isOpened():
    print('Error opening video capture')
    exit(1)

# Define the codec and create VideoWriter object: https://docs.opencv.org/3.4/dd/d9e/classcv_1_1VideoWriter.html
'''
(*'mp4v') -> MPEG-4 Part 14 codec
'''
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

'''
video_capture.get(3) -> Width of the frames in the video stream.
video_capture.get(4) -> Height of the frames in the video stream.
30.0 -> FPS
'''
video_output = cv2.VideoWriter('output/output_demo.mp4', fourcc, 30.0, (int(video_capture.get(3)), int(video_capture.get(4))))

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if not ret:  # If video ends
        break

    # Operate with the frame on gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame with the classifier
    '''
    All the values of the parameters are manually adjusted to get the best results on the demo video...
    '''
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(50, 50), maxSize=(120, 120))

    # Draw a rectangle around the faces detected
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow('Demo video', frame)

    # Write the frame into the output video
    video_output.write(frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and output
video_capture.release()
video_output.release()

# Close all the windows
cv2.destroyAllWindows()
