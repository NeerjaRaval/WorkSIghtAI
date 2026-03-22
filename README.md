WorkSight AI

Intelligent Workforce Monitoring System (Computer Vision + AI)

WorkSight AI is a real-time computer vision system designed to automate workforce monitoring, improve productivity, and enforce workplace compliance using AI-driven insights.

It combines face recognition, gesture analysis, and object detection into a unified, low-latency pipeline capable of running on standard CPU hardware.

==============Key Features==============

    • Face Recognition — Real-time employee identification & tracking
    • Behavior Analysis — Gesture/posture detection for compliance monitoring
    • Object Detection — Identifies critical/restricted items
    • Live Dashboard — Real-time visualization via PyQt6
    • Event Logging — Structured data storage for analytics
    • System Architecture


 ==============Processing Pipeline==============
 
Camera Feed (CCTV / Webcam)
        ↓
Frame Capture (OpenCV)
        ↓
AI Processing Layer
  • Face Recognition
  • Gesture Detection (MediaPipe)
  • Object Detection
        ↓
Decision Engine (Rule-based logic)
        ↓
Database (MySQL / SQLite)
        ↓
GUI Dashboard (PyQt6)


 ==============Tech Stack==============
 
   • Layer	Technology
   • Language	Python 3.x
   • Computer Vision	OpenCV
   • AI Models	MediaPipe, face_recognition (dlib)
   • GUI	PyQt6
   • Database	MySQL / SQLite


==============How It Works==============

 • Captures live video stream from camera/DVR
 • Extracts frames and processes them in real-time
 • Detects faces and matches with stored identities
 • Analyzes gestures & posture using ML models
 • Applies rule-based logic for behavior classification
 • Logs events and updates dashboard


 ==============Engineering Highlights==============
 
 • Multi-model AI integration in a single real-time pipeline
 • Optimized for CPU-only environments
 • Modular architecture for scalability
 • Rule-based decision engine for interpretable outputs


 ==============Use Cases==============
 
 • Workplace productivity monitoring
 • Attendance automation
 • Safety & compliance tracking
 • Behavioral analytics


 ==============Future Improvements==============
 
 • GPU acceleration (CUDA/OpenVINO)
 • Cloud dashboard + remote access
 • Deep learning-based behavior prediction
 • Mobile companion app


🧠 Project Vision

WorkSight AI demonstrates how AI + systems engineering can transform traditional surveillance into intelligent, actionable monitoring systems—bridging the gap between raw video data and meaningful insights.
