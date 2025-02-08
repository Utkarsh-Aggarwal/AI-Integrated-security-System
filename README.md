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
![Screenshot 2025-02-08 154344-Photoroom (1)](https://github.com/user-attachments/assets/4cc64374-5fbd-4bb7-8b0a-1cdd60b00bc8)



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
