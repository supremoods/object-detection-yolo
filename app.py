import cv2
from ultralytics import YOLO

# Load the pre-trained YOLO model
model = YOLO("yolov8s-world.pt")  # Using standard YOLOv8 Nano model

# list of all yolov8
# yolo11n.pt
# yolov8n.pt
# yolov8s-world.py


model.set_classes(['traffic-signs', 'phone'])

# Open the webcam
cap = cv2.VideoCapture(0)

# Check if webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

# Process video frames
while cap.isOpened():
    # Read a frame from the webcam
    success, frame = cap.read()
    
    if not success:
        print("Error: Failed to capture frame")
        break

    # Perform object detection and tracking
    results = model.track(
        source=frame,
        persist=True,       # Maintain tracking between frames
        conf=0.5,           # Minimum confidence threshold
        verbose=False       # Reduce console output
    )
    
    # Visualize the results on the frame
    annotated_frame = results[0].plot()
    
    # Display the processed frame
    cv2.imshow("YOLO Object Tracking", annotated_frame)
    
    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()