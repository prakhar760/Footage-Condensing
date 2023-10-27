import cv2
import os
import time

# Create a VideoCapture object for the webcam/ipcam
cap = cv2.VideoCapture("http://192.168.19.105:4747/video")
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Print the total number of frames
print(f"Total frames: {total_frames}")

# cap = cv2.VideoCapture(0)

# Set the resolution of the captured frames
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) 
cap.set(cv2.CAP_PROP_BUFFERSIZE,3)

# Create a directory to save the captured images and videos
if not os.path.exists("ip_saved_media6"):
    os.makedirs("ip_saved_media6")

# Define the time interval between captures (in seconds)
capture_interval = int(input("Enter Capture Frame Interval: ")) #5

# Define the maximum number of frames to capture before generating a video
max_frames_per_video = int(input("Enter Max Frames For A Video: ")) #30
target_fps = int(input("Enter Target FPS: "))

# Initialize variables for image and video capture
image_frames = []
video_frames = []
start_time = time.time()

# Loop to capture and save images and videos
# Initialize counter variable
counter = 0

while True:
    # Increment the counter
    counter += 1
    
    # Get the current time
    current_time = time.time()

    # Check if it's time to capture an image
    if current_time - start_time >= capture_interval:
        # Capture a frame from the webcam
        ret, frame = cap.read()

        #print(ret)

        # Check if the frame was captured successfully
        if ret:
            # Check if the counter is a multiple of 25  
            if counter % 45 == 0:
                # Save the frame to a file
                filename = f"ip_saved_media6/image_{current_time}.jpg"
                cv2.imwrite(filename, frame)

                # Add the filename to the list of frames for the next video
                image_frames.append(filename)

                # Update the start time
                start_time = current_time

    # Check if it's time to generate a video
    if len(image_frames) >= max_frames_per_video:
        # Define the video filename
        video_filename = f"ip_saved_media5/video_{current_time}.avi"

        # Define the codec and video writer
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        out = cv2.VideoWriter(video_filename, fourcc, target_fps, (640, 480))  #5 is FPS

        # Loop through the frames and add them to the video
        for frame_filename in image_frames:
            frame = cv2.imread(frame_filename)
            out.write(frame)

        # Release the video writer and reset the frames list
        out.release()
        image_frames = []
