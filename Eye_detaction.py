{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-08-02 15:57:49.843 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\vishn\\AppData\\Roaming\\Python\\Python312\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "import streamlit as st\n",
    "from PIL import Image\n",
    "import numpy as np\n",
    "\n",
    "# Load Haar cascade classifiers\n",
    "face_cascade = cv2.CascadeClassifier(r\"C:\\Users\\vishn\\Downloads\\Haarcascades\\Haarcascades\\haarcascade_frontalface_default.xml\")\n",
    "eye_cascade = cv2.CascadeClassifier(r\"C:\\Users\\vishn\\Downloads\\Haarcascades\\Haarcascades\\haarcascade_eye.xml\")\n",
    "\n",
    "# Function to detect faces and eyes\n",
    "def detect_faces_eyes(frame):\n",
    "    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)\n",
    "    faces = face_cascade.detectMultiScale(gray, 1.3, 5)\n",
    "    for (x, y, w, h) in faces:\n",
    "        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)\n",
    "        roi_gray = gray[y:y+h, x:x+w]\n",
    "        roi_color = frame[y:y+h, x:x+w]\n",
    "        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)\n",
    "        for (ex, ey, ew, eh) in eyes:\n",
    "            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)\n",
    "    return frame\n",
    "\n",
    "# Streamlit interface\n",
    "st.title(\"Face and Eye Detection App\")\n",
    "\n",
    "# Add a sidebar for user controls\n",
    "st.sidebar.title(\"Controls\")\n",
    "run = st.sidebar.checkbox('Run')\n",
    "st.sidebar.text(\"Press 'Stop' to end\")\n",
    "\n",
    "# Webcam input and processing\n",
    "FRAME_WINDOW = st.image([])\n",
    "\n",
    "camera = cv2.VideoCapture(0)\n",
    "\n",
    "while run:\n",
    "    _, frame = camera.read()\n",
    "    frame = detect_faces_eyes(frame)\n",
    "    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)\n",
    "    FRAME_WINDOW.image(frame)\n",
    "else:\n",
    "    st.write('Stopped')\n",
    "    camera.release()\n",
    "\n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "streamlit run \n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
#modified some code
