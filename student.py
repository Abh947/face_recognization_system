from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


class student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition system")
        
        #variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_syd_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        
        
        #First image
        
        img = Image.open(r"C:\Users\hp\Desktop\Face recognition\New folder\college images\Shoolini MBA.jpg")
        img = img.resize((500, 130))
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_1bl = Label(self.root,image=self.photoimg)
        f_1bl.place(x = 0, y = 0, width = 500, height = 130)
        
        
        #Second image
        img1 = Image.open(r"C:\Users\hp\Desktop\Face recognition\New folder\college images\shollini student.jpeg")
        img1 = img1.resize((600, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_1bl = Label(self.root,image=self.photoimg1)
        f_1bl.place(x = 500, y = 0, width = 600, height = 130)
        
        
        
        #Third image
        
        img2 = Image.open(r"C:\Users\hp\Desktop\Face recognition\New folder\college images\Student Placementds.jpeg")
        img2 = img2.resize((500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_1bl = Label(self.root,image=self.photoimg2)
        f_1bl.place(x = 1000, y = 0, width = 550, height = 130)
        
        
        #Background image
        
        img4 = Image.open(r"C:\Users\hp\Desktop\Face recognition\New folder\college images\face 5.jpg")
        img4 = img4.resize((1530, 710))
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x = 0, y = 130, width = 1530, height = 710)
        
        
        #title
        title_lbl = Label(bg_img, text = "STUDENT MANAGEMENT SYSTEM", font = ("times new roman", 35, "bold"),bg = "red", fg = "white" )
        title_lbl.place(x = 0, y = 0, width = 1530, height = 45)
        
        
        #Frame
        main_frame = Frame(bg_img, bd = 2, bg = "white")
        main_frame.place(x = 20, y = 50, width = 1480, height = 600)
        
        #Left label frame
        
        Left_frame = LabelFrame(main_frame, bd = 2, bg = "white",  relief = RIDGE, text = "Student Details", font = ('times new roman', 12, "bold"))
        Left_frame.place(x = 10, y = 10, width = 730, height = 580)
        
        
        img_Left = Image.open(r"C:\Users\hp\Desktop\Face recognition\New folder\college images\Student-id.webp")
        img_Left = img_Left.resize((720, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_Left)
        
        f_1bl = Label(Left_frame,image=self.photoimg2)
        f_1bl.place(x = 5, y = 0, width = 720, height = 130)
        
        
        #Current course
        current_course_frame = LabelFrame(Left_frame, bd = 2, bg = "white",  relief = RIDGE, text = "Current course", font = ('times new roman', 12, "bold"))
        current_course_frame.place(x = 5, y = 135, width = 720, height = 150)
        
        #Department
        
        dep_label = Label(current_course_frame, text = "Department", font = ("times new roman", 12, "bold"), bg = "white")
        dep_label.grid(row = 0, column = 0, padx = 10, sticky = W)
        
        dep_combo = ttk.Combobox(current_course_frame,textvariable = self.var_dep, font = ('times new roman', 13, "bold"), state = "read only", width = 20)
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row = 0, column = 1, padx = 2, pady = 10, sticky = W)
        
        #Course
        course_label = Label(current_course_frame, text = "course", font = ("times new roman", 13, "bold"), bg = "white")
        course_label.grid(row = 0, column = 2, padx = 10, sticky = W)
        
        course_combo = ttk.Combobox(current_course_frame,textvariable = self.var_course, font = ("times new roman", 13, "bold"), state = "readonly", width = 20)
        course_combo["values"] = ("select course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row = 0, column = 3, padx = 2, pady = 10, sticky = W)
        
        #Year 
        year_label = Label(current_course_frame, text = "Year", font = ("times new roman", 13, "bold"), bg = "white")
        year_label.grid(row = 1, column = 0, padx = 10, sticky = W)
        
        year_combo = ttk.Combobox(current_course_frame,textvariable = self.var_year, font = ("times new roman", 13, "bold"), state = "readonly", width = 20)
        year_combo["values"] = ("select Year", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25")
        year_combo.current(0)
        year_combo.grid(row = 1, column = 1, padx = 2, pady = 10, sticky = W)
        
        
        #Semester
        semester_label = Label(current_course_frame, text = "course", font = ("times new roman", 13, "bold"), bg = "white")
        semester_label.grid(row = 1, column = 2, padx = 10, sticky = W)
        
        semester_combo = ttk.Combobox(current_course_frame,textvariable = self.var_semester, font = ("times new roman", 13, "bold"), state = "readonly", width = 20)
        semester_combo["values"] = ("select semester", "semester-1", "semester-2", "semester-3", "semester-4")
        semester_combo.current(0)
        semester_combo.grid(row = 1, column = 3, padx = 2, pady = 10, sticky = W)
        
        #Class student information
        class_student_frame = LabelFrame(Left_frame, bd = 2, bg = "white", relief = RIDGE, text = "Class Student Information", font = ('times new roman', 12, "bold"))
        class_student_frame.place(x = 5, y = 250, width = 720, height = 300)
        
        #Student id
        studentID_label = Label(class_student_frame, text = "StudentID:", font = ("times new roman", 13, "bold"), bg = "white")
        studentID_label.grid(row = 0, column = 0, padx = 10, sticky = W)
        
        studentID_entry = ttk.Entry(class_student_frame,textvariable = self.var_syd_id, width = 20, font = ("times new roman", 13, "bold"))
        studentID_entry.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = W)
        
        #Student name
        studentName_label = Label(class_student_frame, text = "Student Name:", font = ("times new roman", 13, "bold"), bg = "white")
        studentName_label.grid(row = 0, column = 2, padx = 10, pady = 5, sticky = W)
        
        studentName_entry = ttk.Entry(class_student_frame,textvariable = self.var_std_name, width = 20, font = ("times new roman", 13, "bold"))
        studentName_entry.grid(row = 0, column = 3, padx = 10, pady = 5, sticky = W)
        
        #Class division
        class_div_label = Label(class_student_frame, text = "Class Division:", font = ("times new roman", 13, "bold"), bg = "white")
        class_div_label.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = W)
        
        class_div_entry = ttk.Entry(class_student_frame,textvariable = self.var_div, width = 20, font = ("times new roman", 13, "bold"))
        class_div_entry.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)
        
        #Roll No
        roll_no_label = Label(class_student_frame, text = "Roll No:", font = ("times new roman", 13, "bold"), bg = "white")
        roll_no_label.grid(row = 1, column = 2, padx = 10, pady = 5, sticky = W)
        
        roll_no_entry = ttk.Entry(class_student_frame,textvariable = self.var_roll, width = 20, font = ("times new roman", 13, "bold"))
        roll_no_entry.grid(row = 1, column = 3, padx = 10, pady = 5, sticky = W)
        
        #Gender
        gender_label = Label(class_student_frame, text = "Gender:", font = ("times new roman", 13, "bold"), bg = "white")
        gender_label.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = W)
        
        gender_entry = ttk.Entry(class_student_frame,textvariable = self.var_gender, width = 20, font = ("times new roman", 13, "bold"))
        gender_entry.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)
        
        #DOB
        dob_label = Label(class_student_frame, text = "DOB:", font = ("times new roman", 13, "bold"), bg = "white")
        dob_label.grid(row = 2, column = 2, padx = 10, pady = 5, sticky = W)
        
        dob_entry = ttk.Entry(class_student_frame,textvariable = self.var_dob, width = 20, font = ("times new roman", 13, "bold"))
        dob_entry.grid(row = 2, column = 3, padx = 10, pady = 5, sticky = W)
        
        #Email
        email_label = Label(class_student_frame, text = "Email:", font = ("times new roman", 13, "bold"), bg = "white")
        email_label.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = W)
        
        email_entry = ttk.Entry(class_student_frame,textvariable = self.var_email, width = 20, font = ("times new roman", 13, "bold"))
        email_entry.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)
        
        #Phone no
        phone_label = Label(class_student_frame, text = "Phone No:", font = ("times new roman", 13, "bold"), bg = "white")
        phone_label.grid(row = 3, column = 2, padx = 10, pady = 5, sticky = W)
        
        phone_entry = ttk.Entry(class_student_frame,textvariable = self.var_phone, width = 20, font = ("times new roman", 13, "bold"))
        phone_entry.grid(row = 3, column = 3, padx = 10, pady = 5, sticky = W)
        
        #Address
        address_label = Label(class_student_frame, text = "Address:", font = ("times new roman", 13, "bold"), bg = "white")
        address_label.grid(row = 3, column = 2, padx = 10, pady = 5, sticky = W)
        address_entry = ttk.Entry(class_student_frame,textvariable = self.var_address, width = 20, font = ("times new roman", 13, "bold"))
        address_entry.grid(row = 3, column = 3, padx = 10, pady = 5, sticky = W)
        
        #Teacher Name
        teacher_label = Label(class_student_frame, text = "Teacher Name:", font = ("times new roman", 13, "bold"), bg = "white")
        teacher_label.grid(row = 4, column = 2, padx = 10, pady = 5, sticky = W)
        teacher_entry = ttk.Entry(class_student_frame,textvariable = self.var_teacher, width = 20, font = ("times new roman", 13, "bold"))
        teacher_entry.grid(row = 4, column = 3, padx = 10, pady = 5, sticky = W)
        
        #Radio buttons
        self.var_radio1 = StringVar()
        Radiobutton1 = ttk.Radiobutton(class_student_frame, text = "Take photo sample", value = "Yes")
        Radiobutton1.grid(row = 5, column = 0)
        
        self.var_radio2 = StringVar()
        Radiobutton2 = ttk.Radiobutton(class_student_frame, text = "No photo sample", value = "No")
        Radiobutton2.grid(row = 5, column = 1)
        
        #Buttons Frame
        button_frame = Frame(class_student_frame, bd = 2, relief = RIDGE, bg = "white")
        button_frame.place(x = 0, y =200, width = 715, height = 32)
        
        save_button = Button(button_frame, text = "Save",command = self.add_data, width = 17,  font = ("times new roman", 13, "bold"), bg = "blue", fg = "white")
        save_button.grid(row = 0, column = 0)
        
        update_button = Button(button_frame, text = "Update", width = 17,  font = ("times new roman", 13, "bold"), bg = "blue", fg = "white")
        update_button.grid(row = 0, column = 1)
        
        
        delete_button = Button(button_frame, text = "Delete", width = 17,  font = ("times new roman", 13, "bold"), bg = "blue", fg = "white")
        delete_button.grid(row = 0, column = 2)
        
        reset_button = Button(button_frame, text = "Reset", width = 17,  font = ("times new roman", 13, "bold"), bg = "blue", fg = "white")
        reset_button.grid(row = 0, column = 3)
        
        button_frame1 = Frame(class_student_frame, bd = 2, relief = RIDGE, bg = "white")
        button_frame1.place(x = 0, y = 235, width = 715, height = 32)
        
        take_photo_button = Button(button_frame1, text = "Take Photo Sample", width = 35,  font = ("times new roman", 13, "bold"), bg = "blue", fg = "white")
        take_photo_button.grid(row = 1, column = 0)
        
        update_photo_button = Button(button_frame1, text = "Update Photo Sample", width = 35,  font = ("times new roman", 13, "bold"), bg = "blue", fg = "white")
        update_photo_button.grid(row = 1, column = 1)
        
        #Right label frame
        
        Right_frame = LabelFrame(main_frame, bd = 2, bg = "white",  relief = RIDGE, text = "Student Details", font = ('times new roman', 12, "bold"))
        Right_frame.place(x = 750, y = 10, width = 720, height = 580)
        
        img_right = Image.open(r"C:\Users\hp\Desktop\Face recognition\New folder\college images\admission.webp")
        img_right = img_right.resize((720, 130))
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        f_1bl = Label(Right_frame,image=self.photoimg_right)
        f_1bl.place(x = 5, y = 0, width = 720, height = 130)
        
        #Search system
        
        Search_frame = LabelFrame(Right_frame, bd = 2, bg = "white", relief = RIDGE, text = "Search System", font = ('times new roman', 12, "bold"))
        Search_frame.place(x = 5, y = 135, width = 710, height = 70)
        
        search_label = Label(Search_frame, text = "Search By:", font = ("times new roman", 15, "bold"), bg = "white")
        search_label.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = W)
        
        search_combo = ttk.Combobox(Search_frame, font = ("times new roman", 13, "bold"), state = "readonly", width = 20)
        search_combo["values"] = ("select", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row = 0, column = 1, padx = 2, pady = 10, sticky = W)
        
        
        search_entry = ttk.Entry(Search_frame, width = 15,  font = ("times new roman", 13, "bold"))
        search_entry.grid(row = 0, column = 2, padx = 10, pady = 5, sticky = W)
        
        
        
        search_button = Button(button_frame, text = "search", width = 12,  font = ("times new roman", 13, "bold"), bg = "blue", fg = "white")
        search_button.grid(row = 0, column = 3, padx = 4)
        
        showAll_button = Button(button_frame, text = "showAll", width = 12,  font = ("times new roman", 13, "bold"), bg = "blue", fg = "white")
        showAll_button.grid(row = 0, column = 4, padx = 4)
        
        #Table frame
        
        table_frame = Frame(Right_frame, bd = 2, bg = "white", relief = RIDGE)
        table_frame.place(x = 5, y = 210, width = 710, height = 350)
        
        scroll_x = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient = VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame, column = ("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)
        
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)
        scroll_x.config(command = self.student_table.xview)
        scroll_y.config(command = self.student_table.yview)
        
        self.student_table.heading("dep",text = "Department")
        self.student_table.heading("course",text = "Course")
        self.student_table.heading("year",text = "Year")
        self.student_table.heading("sem",text = "Semester")
        self.student_table.heading("id",text = "Student Id")
        self.student_table.heading("name",text = "Name")
        self.student_table.heading("div",text = "Division")
        self.student_table.heading("dob",text = "DOB")
        self.student_table.heading("email",text = "Email")
        self.student_table.heading("phone",text = "Phone")
        self.student_table.heading("address",text = "Address")
        self.student_table.heading("photo",text = "PhotoSampleStatus")
        self.student_table["show"] = "headings"
        self.student_table.column("dep", width = 100)
        self.student_table.column("course", width = 100)
        self.student_table.column("year", width = 100)
        self.student_table.column("sem", width = 100)
        self.student_table.column("id", width = 100)
        self.student_table.column("name", width = 100)
        self.student_table.column("roll", width = 100)
        self.student_table.column("gender", width = 100)
        self.student_table.column("div", width = 100)
        self.student_table.column("email", width = 100)
        self.student_table.column("phone", width = 100)
        self.student_table.column("address", width = 100)
        self.student_table.column("teacher", width = 100)
        self.student_table.column("photo", width = 100)
        self.student_table.pack(fill = BOTH, expand = 1)
        
        
    #function decration
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent = self.root) 
        else:
            pass    
        
       
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()
        