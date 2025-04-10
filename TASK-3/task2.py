import cv2
from ultralytics import YOLO

# Load your YOLO model (change the path if needed)
model = YOLO("yolov8s.pt")  # or "your_custom_model.pt"

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

# Set resolution (optional)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO prediction
    results = model.predict(frame, conf=0.5)  # You can adjust confidence threshold

    # Draw the results
    annotated_frame = results[0].plot()

    # Show the frame
    cv2.imshow("Webcam - YOLOv8 Detection", annotated_frame)

    # Exit with ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
