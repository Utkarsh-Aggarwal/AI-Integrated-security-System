# AI-Integrated-security-System
This repository contains the code and implementation details for a Facial Recognition-Based Security System using Python, OpenCV, DeepFace, and an ESP32 microcontroller. The system provides secure access control by authenticating users through facial recognition and controlling a solenoid lock via a relay module.

Smart Facial Recognition Security System with Solenoid Lock
This repository contains the code and implementation details for a Facial Recognition-Based Security System using Python, OpenCV, DeepFace, and an ESP32 microcontroller. The system provides secure access control by authenticating users through facial recognition and controlling a solenoid lock via a relay module.

Features
✅ Facial Recognition Authentication – Uses DeepFace for real-time face matching.
✅ Two-Factor Authentication (2FA) – Requests a password if facial recognition fails.
✅ Solenoid Lock Control – Unlocks when access is granted, remains locked otherwise.
✅ ESP32 Integration – Communicates via serial to control the lock and LED indicators.
✅ LED Indicators – Green LED for access granted, Red LED for access denied.
✅ Email Alerts – Sends an email with a screenshot when an unauthorized user attempts access.
✅ Configurable Lock Duration – Keeps the solenoid lock retracted for a defined period before returning to the locked state.

Hardware Requirements
ESP32 (38-pin) microcontroller
5V Relay Module
12V Solenoid Lock
Webcam for face detection
LEDs (Red & Green) with 220Ω resistors
12V Power Supply
Software Requirements
Python 3.x
OpenCV
DeepFace
Serial Communication (pyserial)
SMTP for email alerts
Arduino IDE for ESP32 programming

Block diagram:
![WhatsApp Image 2025-02-08 at 18 41 09_62ef361a](https://github.com/user-attachments/assets/62377930-2f95-433d-96c2-44449fb7bc3a)

Schematic diagram:
![WhatsApp Image 2025-02-08 at 18 40 53_23de9f62](https://github.com/user-attachments/assets/e6f65ed6-da2f-4f4b-bed7-46ec5f9d78b2)



📂 Facial-Recognition-Security-System  
 ├── 📁 face_data/              # Stored face images  
 ├── 📜 security_system.py      # Python script for face recognition & authentication  
 ├── 📜 esp32_code.ino          # Arduino code for solenoid control  
 ├── 📜 requirements.txt        # Required Python dependencies  
 ├── 📜 README.md               # Project Documentation  
Future Improvements
🔹 IoT integration for remote access
🔹 Mobile app for real-time control
🔹 Improved AI-based recognition for better accuracy

🚀 Contributions are welcome! Feel free to fork the repo, submit issues, and suggest improvements.
