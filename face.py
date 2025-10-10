import os
import cv2
import numpy as np
import pandas as pd
from datetime import datetime

class FaceRecognizer:
    def __init__(self, model_path='trainer.yml', labels_path='labels.txt', attendance_file='attendance.csv'):
        self.model_path = model_path
        self.labels_path = labels_path
        self.attendance_file = attendance_file
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read(self.model_path)
        self.names = self.load_labels()

    def load_labels(self):
        names = {}
        with open(self.labels_path, 'r') as f:
            for line in f:
                id_str, name = line.strip().split(":")
                names[int(id_str)] = name
        return names

    def mark_attendance(self, name):
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")

        if not os.path.exists(self.attendance_file):
            with open(self.attendance_file, 'w') as f:
                f.write("Name,Date,Time\n")

        df = pd.read_csv(self.attendance_file)
        if not ((df['Name'] == name) & (df['Date'] == date_str)).any():
            with open(self.attendance_file, 'a') as f:
                f.write(f"{name},{date_str},{time_str}\n")
            print(f"[ATTENDANCE] {name} marked at {time_str}")

    def start_recognition(self):
        cap = cv2.VideoCapture(0)
        marked = set()

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            for (x, y, w, h) in faces:
                id_, confidence = self.recognizer.predict(gray[y:y+h, x:x+w])
                name = "Unknown"
                if confidence < 70:
                    name = self.names.get(id_, "Unknown")
                    if name not in marked:
                        self.mark_attendance(name)
                        marked.add(name)

                cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
                cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

            cv2.imshow("Face Recognition Attendance", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    fr = FaceRecognizer()
    fr.start_recognition()
