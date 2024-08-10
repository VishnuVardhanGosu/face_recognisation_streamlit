import cv2
import streamlit as st
from PIL import Image
import numpy as np

# Load Haar cascade classifiers
face_cascade = cv2.CascadeClassifier(r"C:\Users\vishn\Downloads\Haarcascades\Haarcascades\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"C:\Users\vishn\Downloads\Haarcascades\Haarcascades\haarcascade_eye.xml")

# Function to detect faces and eyes
def detect_faces_eyes(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)
    return frame

# Streamlit interface
st.title("Face and Eye Detection App")
st.subheader("A Real-Time Face and Eye Detection Application")

# Custom CSS to change the background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: 	#F0F8FF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Information and Instructions
st.markdown("""
    Welcome to the Face and Eye Detection App! This application uses your webcam to detect faces and eyes in real-time using OpenCV's Haar cascades.
    
            **Note:** Ensure that your webcam is accessible and allowed by your browser.
""")

# Initialize session state for running status
if 'run' not in st.session_state:
    st.session_state.run = False

def start():
    st.session_state.run = True

def stop():
    st.session_state.run = False

# Webcam input and processing
FRAME_WINDOW = st.image([])

camera = cv2.VideoCapture(0)

# Run the webcam if the 'run' state is True
if st.session_state.run:
    while True:
        ret, frame = camera.read()
        if not ret:
            st.error("Failed to capture image")
            break
        frame = detect_faces_eyes(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
        # Break the loop if 'run' is set to False
        if not st.session_state.run:
            break
else:
    st.write('Click "Start" to start the webcam')

camera.release()

# Place buttons side by side
col1, col2 = st.columns(2)
with col1:
    st.button("Start", on_click=start)
with col2:
    st.button("Stop", on_click=stop)




