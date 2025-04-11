# Semicore-Assessment
This project focuses on building a real-time car parking detection and human behavior monitoring system using YOLOv8 and OpenCV. It was developed in multiple stages as outlined below:
Link for the output Videos of all tasks: https://drive.google.com/drive/folders/1VLlRSD5n5-CCqJrnAKnj4AHiGhvyTTej?usp=sharing

✅ Task 1: YOLOv8 Integration with Video Input
Implemented YOLOv8 to detect cars in a parking lot from a recorded video (parking1.mp4).

Defined 12 parking slot areas manually using polygon coordinates.

Detected whether each slot was occupied or empty based on whether a car’s center point fell inside a defined zone.

Displayed the number of free slots on the video in real-time, with visual cues (red for occupied, green for empty).

✅ Task 2: Real-Time Detection with Webcam (Edge Device Simulation)


**Objective:**  
Implement real-time vehicle detection using webcam input to simulate an edge device (e.g., Raspberry Pi or Jetson Nano).

**Status:**  
❌ Not implemented yet

**Next Steps:**  
- Integrate YOLOv8 model for live webcam input.  
- Reuse slot-detection logic from Task 1.  
- Optimize processing to run efficiently on low-power hardware.

📌 This task will enhance the system by making it deployable in live environments.


✅ Task 3: Suspicious Human Activity Detection from Video
Extended the system to monitor suspicious behavior of humans using a video input (e.g. CCTV feed).

The YOLOv8 model detects people and monitors their behavior patterns.

Custom logic (based on time spent in certain areas, loitering, or posture) was applied to flag suspicious activity such as:

Prolonged presence in restricted areas

Repeated pacing or motion patterns

Unusual posture or crouching (optional future implementation)

Triggered visual alerts (e.g., red boxes or warning messages) when suspicious activity was detected.

This feature enhances the parking monitoring system by adding a layer of security surveillance.




├── common/                       # Shared files if needed later
│   └── shared_utils.py
│
├── requirements.txt
└── README.md                     # Main project summary with task links

