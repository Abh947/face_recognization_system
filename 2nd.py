from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import student # Ensure you have a `student.py` file with a `student` class in the same directory
from developer import Developer
class Face_Recognition_system:
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # First image
        img = Image.open(r"C:\Users\hp\Desktop\Face recognition\New folder\college images\shollini.jpg")
        img = img.resize((500, 130))
        self.photoimg = ImageTk.PhotoImage(img)
        f_1bl = Label(self.root, image=self.photoimg)
        f_1bl.place(x=0, y=0, width=500, height=130)
        
        # Second image
        img1 = Image.open(r"C:\Users\hp\Desktop\Face recognition\New folder\college images\face 1.jpg")
        img1 = img1.resize((600, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_1bl = Label(self.root, image=self.photoimg1)
        f_1bl.place(x=500, y=0, width=600, height=130)
        
        # Third image
        img2 = Image.open(r"C:\Users\hp\Desktop\Face recognition\New folder\college images\shoolini 2.jpeg")
        img2 = img2.resize((500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_1bl = Label(self.root, image=self.photoimg2)
        f_1bl.place(x=1000, y=0, width=550, height=130)
        
        # Background image
        img4 = Image.open(r"C:\Users\hp\Desktop\Face recognition\New folder\college images\face 5.jpg")
        img4 = img4.resize((1530, 710))
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        # Title
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Student Button
        img5 = Image.open(r"C:\Users\hp\Desktop\Face recognition\New folder\college images\face 8.jpg")
        img5 = img5.resize((220, 220))
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img, image=self.photoimg5, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)
        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        # Face Detector Button
        img6 = Image.open(r"C:\Users\hp\Desktop\Face recognition\New folder\college images\face 6.jpeg")
        img6 = img6.resize((220, 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b2 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b2.place(x=500, y=100, width=220, height=220)
        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b2_1.place(x=500, y=300, width=220, height=40)

        # Attendance Button
        img7 = Image.open(r"C:\Users\hp\Desktop\Face recognition\New folder\college images\attendce.webp")
        img7 = img7.resize((220, 220))
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b3 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b3.place(x=800, y=100, width=220, height=220)
        b3_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_1.place(x=800, y=300, width=220, height=40)

        # Help Desk Button
        img8 = Image.open(r"C:\Users\hp\Desktop\Face recognition\New folder\college images\help.jpg")
        img8 = img8.resize((220, 220))
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b4 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        b4.place(x=1100, y=100, width=220, height=220)
        b4_1 = Button(bg_img, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b4_1.place(x=1100, y=300, width=220, height=40)

        # Train Data Button
        img9 = Image.open(r"C:\Users\hp\Desktop\Face recognition\New folder\college images\train data.jpg")
        img9 = img9.resize((220, 220))
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b5 = Button(bg_img, image=self.photoimg9, cursor="hand2")
        b5.place(x=200, y=380, width=220, height=220)
        b5_1 = Button(bg_img, text="Train Data", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b5_1.place(x=200, y=580, width=220, height=40)

        # Photos Button
        img10 = Image.open(r"C:\Users\hp\Desktop\Face recognition\New folder\college images\Photos.jpg")
        img10 = img10.resize((220, 220))
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b6 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b6.place(x=500, y=380, width=220, height=220)
        b6_1 = Button(bg_img, text="Photos", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b6_1.place(x=500, y=580, width=220, height=40)

        # Developer Button
        img11 = Image.open(r"C:\Users\hp\Desktop\Face recognition\New folder\college images\developer.jpg")
        img11 = img11.resize((220, 220))
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b7 = Button(bg_img, image=self.photoimg11,command=self.developer_details, cursor="hand2")
        b7.place(x=800, y=380, width=220, height=220)
        b7_1 = Button(bg_img, text="Developer",command=self.developer_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b7_1.place(x=800, y=580, width=220, height=40)

        # Exit Button
        img12 = Image.open(r"C:\Users\hp\Desktop\Face recognition\New folder\college images\exit.jpg")
        img12 = img12.resize((220, 220))
        self.photoimg12 = ImageTk.PhotoImage(img12)
        b8 = Button(bg_img, image=self.photoimg12, cursor="hand2")
        b8.place(x=1100, y=380, width=220, height=220)
        b8_1 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b8_1.place(x=1100, y=580, width=220, height=40)
        
        #Functions button

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)
        
        #developer
    def developer_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_system(root)
    root.mainloop()
