import cv2

# IP camera URL
url = "http://192.168.19.105:4747/video"

# Open a video capture object
cap = cv2.VideoCapture(url)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Cannot connect to IP camera")
    exit()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('input2.avi', fourcc, 20.0, (640, 480))

# Loop through frames and write them to the output file
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if ret:
        # Display the captured frame for testing purposes
        cv2.imshow('frame', frame)
        
        # Write the frame to the output file
        out.write(frame)
        
        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the capture and output objects
cap.release()
out.release()

# Close all windows
cv2.destroyAllWindows()

# Set target duration and fps
target_duration = int(input("Enter Target Duration: ")) # 30
target_fps = int(input("Enter Target FPS: "))# 1

# Set input and output video paths
input_path = "input2.avi"
output_path = "output_video2.avi"

# Open input video file
input_video = cv2.VideoCapture(input_path)

# Get input video properties
frame_count = int(input_video.get(cv2.CAP_PROP_FRAME_COUNT)) # Total Framce Count
fps = int(input_video.get(cv2.CAP_PROP_FPS)) # FPS
length_in_secs = frame_count / fps 

# Calculate skip frames interval
skip_frames_interval = int((frame_count / target_duration) / target_fps) # Avg FPS (given a duration) / target FPS

# Get input video frame size
frame_width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create output video file
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output_video = cv2.VideoWriter(output_path, fourcc, target_fps, (frame_width, frame_height))

# Process video frames and write to output file
frame_number = 0
while input_video.isOpened():
    ret, frame = input_video.read()
    if not ret:
        break
    if frame_number % skip_frames_interval == 0:
        output_video.write(frame)
    frame_number += 1

# Release video objects
input_video.release()
output_video.release()

# Print output video duration
print(f"Input video duration: {length_in_secs} seconds")
print(f"Output video duration: {target_duration} seconds")


