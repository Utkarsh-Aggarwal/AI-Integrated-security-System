import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from deepface import DeepFace
import cv2
import os
import serial
import time

# Initialize the serial connection to ESP32
ser = serial.Serial('COM11', 115200)  # Replace 'COM11' with your actual ESP32 port
time.sleep(2)  # Wait for the serial connection to initialize

# Email function to send the screenshot (if needed)
def send_email_with_screenshot(to_email, subject, body, screenshot_path):
    from_email = 'alert.alarms.permission@gmail.com'
    password = 'mrjw uozu ynve arjb'  # Use your app password here

    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    with open(screenshot_path, "rb") as attachment:
        mime_base = MIMEBase('application', 'octet-stream')
        mime_base.set_payload(attachment.read())
        encoders.encode_base64(mime_base)
        mime_base.add_header('Content-Disposition', f'attachment; filename={os.path.basename(screenshot_path)}')
        message.attach(mime_base)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        text = message.as_string()
        server.sendmail(from_email, to_email, text)

    print("Email with screenshot sent successfully.")

# Open the camera and capture an image
cap = cv2.VideoCapture(0)
stored_faces = os.listdir('face_data')

if not stored_faces:
    print("No face data found. Please capture face data first.")
    exit()

print("Capturing face for security clearance...")
ret, frame = cap.read()
if not ret:
    print("Failed to capture image.")
    exit()

# Save the captured image temporarily
temp_image_path = "temp_image.jpg"
cv2.imwrite(temp_image_path, frame)

# Preprocess captured image
img = cv2.imread(temp_image_path)
if img is None:
    print("Error: Failed to load the captured image.")
    exit()
img = cv2.resize(img, (224, 224))  # Resize to standard dimensions
cv2.imwrite(temp_image_path, img)

# Verify the face with stored data
clearance_granted = False
confidence_threshold = 0.6

for face_file in stored_faces:
    stored_face_path = os.path.join("face_data", face_file)
    try:
        # Preprocess stored face
        stored_img = cv2.imread(stored_face_path)
        if stored_img is None:
            print(f"Error: Could not read stored face image: {stored_face_path}")
            continue
        stored_img = cv2.resize(stored_img, (224, 224))
        temp_stored_path = "temp_stored_face.jpg"
        cv2.imwrite(temp_stored_path, stored_img)

        # Compare faces
        print(f"Comparing captured image with stored image: {stored_face_path}")
        result = DeepFace.verify(img1_path=temp_image_path, img2_path=temp_stored_path, model_name="VGG-Face")
        print(f"Comparison result: {result}")

        if result["verified"] and result["distance"] <= confidence_threshold:
            clearance_granted = True
            break
    except Exception as e:
        print(f"Error comparing faces: {e}")
        continue

# Communicate the result to the ESP32
if clearance_granted:
    print("Security clearance granted!")
    ser.write(b'GRANTED\n')  # Send "GRANTED" to ESP32
    time.sleep(5)  # Delay for 5 seconds to keep the solenoid lock active
    ser.write(b'LOCK\n')  # Send "LOCK" to explicitly lock and avoid unnecessary pulses
else:
    print("Face not recognized. Please enter the password.")
    send_email_with_screenshot(
        to_email="utkarshaggarwal06@gmail.com",  # Replace with your email
        subject="Intruder Alert!",
        body="An unrecognized person attempted to unlock the system.",
        screenshot_path=temp_image_path
    )
    password = input("Enter the password: ")
    if password == "1234":  # Replace with your desired password
        print("Security clearance granted!")
        ser.write(b'GRANTED\n')  # Send "GRANTED" to ESP32
        time.sleep(5)  # Delay for 5 seconds to keep the solenoid lock active
        ser.write(b'LOCK\n')  # Send "LOCK" to explicitly lock and avoid unnecessary pulses
    else:
        print("Access denied.")
        ser.write(b'LOCK\n')  # Send "LOCK" to ensure the lock remains closed

# Release resources and clean up
cap.release()
cv2.destroyAllWindows()
os.remove(temp_image_path)
