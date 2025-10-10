import cv2
import face_recognition
import numpy as np
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import threading

class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Face Recognition System")

        # Initialize variables
        self.video_source = 0  # Default webcam
        self.known_face_encodings = []  # List to hold known face encodings
        self.known_face_names = []  # List to hold known face names

        # Load known faces
        self.load_known_faces()

        # Start video capture
        self.video_thread = threading.Thread(target=self.video_loop)
        self.video_thread.start()

        # Create a button to recognize faces
        self.recognize_button = Button(self.root, text="Recognize Faces", command=self.recognize_faces)
        self.recognize_button.pack()

    def load_known_faces(self):
        # Load known face images and their encodings
        known_image = face_recognition.load_image_file("path_to_known_face.jpg")  # Replace with your image path
        known_face_encoding = face_recognition.face_encodings(known_image)[0]
        self.known_face_encodings.append(known_face_encoding)
        self.known_face_names.append("Known Person")  # Replace with the person's name

    def video_loop(self):
        # Capture video from the webcam
        self.video_capture = cv2.VideoCapture(self.video_source)
        while True:
            ret, frame = self.video_capture.read()
            if not ret:
                break

            # Convert the image from BGR to RGB
            rgb_frame = frame[:, :, ::-1]

            # Find all the faces and face encodings in the current frame
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            # Loop through each face found in the frame
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                name = "Unknown"

                # If a match was found, use the name of the first match
                if True in matches:
                    first_match_index = matches.index(True)
                    name = self.known_face_names[first_match_index]

                # Draw a rectangle around the face and label it
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            # Display the resulting frame
            cv2.imshow('Video', frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the video capture and close windows
        self.video_capture.release()
        cv2.destroyAllWindows()

    def recognize_faces(self):
        # This function can be expanded to handle additional recognition logic if needed
        print("Recognizing faces...")

if __name__ == "__main__":
    root = Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()