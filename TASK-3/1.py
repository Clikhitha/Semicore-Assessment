import cv2
from ultralytics import YOLO

# Load your custom model
model = YOLO("yolov8s.pt")  # Make sure this detects both 'car' and 'parking_slot'

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    frame = cv2.resize(frame, (1020, 600))

    # Run prediction
    results = model.predict(frame, conf=0.5)
    boxes = results[0].boxes
    class_names = model.names

    total_slots = 0
    car_count = 0

    for box in boxes:
        cls_id = int(box.cls[0])
        class_name = class_names[cls_id]

        x1, y1, x2, y2 = map(int, box.xyxy[0])
        
        if class_name == "parking_slot":
            total_slots += 1
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 0), 2)
            cv2.putText(frame, "slot", (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

        elif class_name == "car":
            car_count += 1
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, "car", (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    empty_slots = max(total_slots - car_count, 0)

    # Display counts
    cv2.putText(frame, f"Total Slots: {total_slots}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.putText(frame, f"Occupied: {car_count}", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    cv2.putText(frame, f"Empty: {empty_slots}", (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Parking Slot Detection", frame)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
