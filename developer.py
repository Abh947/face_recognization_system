from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="blue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Load image safely
        try:
            img_top = Image.open("college_images/facialrecognition.png")
        except FileNotFoundError:
            img_top = Image.new("RGB", (1530, 325), color="gray")

        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        # Frame
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=500, height=600)

        try:
            img_top1 = Image.open("college_images/face2.jpg")
        except FileNotFoundError:
            img_top1 = Image.new("RGB", (200, 200), color="lightgray")

        img_top1 = img_top1.resize((200, 200), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl1 = Label(main_frame, image=self.photoimg_top1)
        f_lbl1.place(x=150, y=0, width=200, height=200)

        # Developer info
        dev_label = Label(main_frame, text="Hello, My Name is Ritik", font=("times new roman", 15, "bold"), bg="white")
        dev_label.place(x=10, y=220)

        dev_label2 = Label(main_frame, text="I'm the developer of this Face Recognition System", font=("times new roman", 12), bg="white")
        dev_label2.place(x=10, y=260)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
