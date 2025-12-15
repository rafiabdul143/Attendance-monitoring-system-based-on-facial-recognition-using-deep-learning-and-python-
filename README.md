  # Attendance-monitoring-system-based-on-facial-recognition-using-deep-learning-and-python 


The **Attendance Monitoring System** based on facial recognition using deep learning and Python employs both deep learning techniques and traditional machine learning models to ensure accurate, real-time attendance tracking. One of the key components utilized in this project is the **Haar Cascade Classifier**, which is a machine learning-based approach used for detecting objects in images or video streams, specifically faces in this case. Here's how the system integrates these components:

### **Haar Cascade Classifier** as Part of the Face Detection:
- The **Haar Cascade Classifier**, provided by **OpenCV**, is used in this system for face detection. This classifier is not part of deep learning but rather a more traditional, efficient method based on the **Haar feature-based cascade classifiers** technique.
- The Haar Cascade works by training on numerous positive and negative images to classify face regions from non-face regions in real-time, making it ideal for the initial stage of face detection in the attendance system.
- It operates by sliding over the image and checking the region of interest for specific features (like eyes, nose, and mouth) using edge detection.

### Integration with Deep Learning:
- After detecting the face using the Haar Cascade Classifier, the **deep learning** model takes over for **face recognition**.
- The system utilizes a **Convolutional Neural Network (CNN)**-based face recognition model, such as the one provided by the **face_recognition** library. This deep learning model extracts facial embeddings and compares them with stored data to identify individuals.
- The **face_recognition** library uses deep neural networks (DNNs) trained on a large dataset to map a person’s face to a unique vector (known as an embedding), allowing for accurate matching even under varied lighting conditions or angles.

### Python Libraries Involved:
- **OpenCV (cv2)**: Used for both image processing tasks and implementing the **Haar Cascade Classifier** for face detection.
- **face_recognition**: A deep learning-based library that handles the task of identifying faces after detection.
- **Pillow (PIL)**: Handles image manipulation tasks, including loading, saving, and resizing images.
- **numpy**: Used for handling arrays and numerical computations that are critical for deep learning and image processing tasks.
- **mysql.connector**: Stores the attendance data in a database, allowing for easy retrieval and reporting.
- **smtplib**: Sends emails automatically (e.g., notifications) when certain events, such as attendance, are recorded.

### Workflow Summary:
1. **Face Detection with Haar Cascade**: Initially, the system detects faces in the input video stream or image using the Haar Cascade Classifier.
2. **Face Recognition with Deep Learning (CNN)**: After the face is detected, a CNN-based deep learning model is applied to recognize the individual by comparing their face with stored embeddings.
3. **Attendance Logging**: The recognized face is logged into the system, and the attendance is recorded in a MySQL database.

By combining traditional machine learning (Haar Cascade) with modern deep learning techniques (CNN), this system ensures both speed and accuracy in face detection and recognition, making it highly effective for real-time attendance monitoring applications.




LIBRARIES USED IN THIS PROJECT
- **Tkinter**: For creating the graphical user interface (GUI).\n
- **PIL (Pillow)**: For image processing tasks.\n
- **cv2 (OpenCV)**: For computer vision tasks, such as face recognition.\n
- **numpy**: For handling numerical operations.\n
- **mysql.connector**: For database connectivity.\n
- **datetime**: For managing date and time operations.\n
- **webbrowser**: For opening URLs from the application.\n
- **face_recognition**: For the core face recognition functionality.\n
- **os**: For interacting with the operating system (file management).\n
- **shutil**: For file and directory operations.\n
- **time**: For implementing time delays and timestamps.\n
- **logging**: For error tracking and logging events in the system.\n
- **threading**: For managing tasks concurrently in the application.\n
- **tkinter.messagebox**: For displaying alert and confirmation dialogs within the GUI."
- smtplib: For sending emails through SMTP


COMMANDS TO INSTALL LIBRARIES.
# For Pillow (PIL)
pip install Pillow

# For OpenCV (cv2)
pip install opencv-python

# For NumPy
pip install numpy

# For MySQL Connector
pip install mysql-connector-python

# For Face Recognition
pip install face_recognition

# For smtplib (part of Python's standard library, no installation required)

# For webbrowser, os, shutil, datetime, time, logging, threading, tkinter.messagebox (These are also part of Python's standard library, no installation required)

