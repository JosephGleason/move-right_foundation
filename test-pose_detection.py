#!/usr/bin/python3

import cv2
import mediapipe as mp
import numpy as np

# Initilize mediapipe
mp_pose = mp.solutions.pose # pose detect model
mp_drawing = mp.solutions.drawing_utils # drawing helper
pose = mp_pose.Pose() # start up ai

print("Welcome to MoveRight")
print("Starting camera... Press 'quit' to quit")

# Start camera
cap = cv2.VideoCapture(0) # use camera #0

# check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera")
    print("Try connecting an external camera or check camera permissions")
    exit()

# counter for photos taken    
fame_count = 0

# infinite loop: taking one photo
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame")
        break

# count this frame and keep track    
    frame_count += 1

# Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# send image to mediapipe ai
    results = pose.process(rgb_frame)
    
    # body points mediapipe found
    if results.pose_landmarks:
        # draw skeleton on the image
        mp_drawing.draw_landmarks(
            frame, # image to draw on
            results.pose_landmarks, # 33 body points to draw
            mp_pose.POSE_CONNECTIONS, # which points connect with lines
            mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=(0, 0, 255), thickenss=2)
            
        )
        
        cv2.putText(frame, "pose detected", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv2.putText(frame, f"Frame: {frame_count}", (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
