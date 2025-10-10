import os
import cv2
import numpy as np

class FaceTrainer:
    def __init__(self, data_path='faces', model_path='trainer.yml'):
        self.data_path = data_path
        self.model_path = model_path
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()  # Requires opencv-contrib-python

    def load_images(self):
        """Load images and labels from the dataset folder"""
        faces = []
        labels = []
        label_map = {}
        current_label = 0

        for folder_name in sorted(os.listdir(self.data_path)):
            folder_path = os.path.join(self.data_path, folder_name)
            if os.path.isdir(folder_path):
                label_map[current_label] = folder_name
                for filename in os.listdir(folder_path):
                    image_path = os.path.join(folder_path, filename)
                    image = cv2.imread(image_path)
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    faces_detected = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

                    for (x, y, w, h) in faces_detected:
                        face = gray[y:y+h, x:x+w]
                        faces.append(face)
                        labels.append(current_label)

                current_label += 1

        return faces, labels, label_map

    def train_model(self):
        """Train the model and save it as trainer.yml"""
        faces, labels, label_map = self.load_images()
        print(f"[INFO] Loaded {len(faces)} face images.")

        if faces and labels:
            self.recognizer.train(faces, np.array(labels))
            self.recognizer.save(self.model_path)
            print(f"[INFO] Model saved as {self.model_path}")
            print("[INFO] Label map:", label_map)
        else:
            print("[ERROR] No faces detected, training cannot proceed.")

if __name__ == "__main__":
    trainer = FaceTrainer()
    trainer.train_model()
