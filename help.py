import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def open_helpdesk():
    help_win = tk.Toplevel()
    help_win.title("Help Desk - Face Recognition Attendance")
    help_win.geometry("800x500")

    # Load background image
    bg_image = Image.open("istockphoto-2149530993-612x612.jpg")
    bg_image = bg_image.resize((800, 500), Image.ANTIALIAS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a label to hold the background
    bg_label = tk.Label(help_win, image=bg_photo)
    bg_label.image = bg_photo  # Keep a reference
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Title on top of the image
    title = tk.Label(help_win, text="Help Desk - Face Recognition Attendance System", 
                     font=("Helvetica", 20, "bold"), bg='#001F3F', fg='white')
    title.place(x=60, y=20)

    # Help text
    instructions = """
Welcome to the Face Recognition Attendance System!

1. Take Images:
   - Click 'Take Images'
   - Enter your ID and Name
   - Face the camera properly and hold still

2. Train Images:
   - After capturing, click 'Train Images'
   - This will process your face data for recognition

3. Track Images:
   - Click 'Track Images' to start face recognition and mark attendance

4. Attendance Sheet:
   - View or export attendance from this section

For support, contact:
Ritik Sharma
ritik.support@university.edu
"""

    help_text = tk.Text(help_win, wrap="word", font=('Arial', 12), bg='#003366', fg='white', bd=0,
                        height=15, width=75)
    help_text.insert(tk.END, instructions)
    help_text.config(state='disabled')
    help_text.place(x=60, y=80)

    # Close button
    close_btn = tk.Button(help_win, text="Close", command=help_win.destroy,
                          font=("Arial", 12, "bold"), bg='red', fg='white', padx=10, pady=5)
    close_btn.place(x=360, y=450)