import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Student Biodata")
window.geometry("800x780")
window.configure(bg="cornsilk2")
window.resizable(False, False)

title = tkinter.Label(
    window,
    text="Student Biodata Form",
    font=("Arial", 18, "bold"),
    bg="bisque3",
    fg="black"
)
title.place(x=200, y=20)

# Labels and Entry boxes
name_label = tkinter.Label(window, text="Name:", bg="azure", font=("Serif", 10))
name_label.place(x=60, y=80)
name_entry = tkinter.Entry(window, width=30, bg="white")
name_entry.place(x=300, y=80)

department_label = tkinter.Label(window, text="Department:", bg="azure", font=("Serif", 10))
department_label.place(x=60, y=120)
department_entry = tkinter.Entry(window, width=30, bg="white")
department_entry.place(x=300, y=120)

email_label = tkinter.Label(window, text="Email:", bg="azure", font=("Serif", 10))
email_label.place(x=60, y=160)
email_entry = tkinter.Entry(window, width=30, bg="white")
email_entry.place(x=300, y=160)

student_id_label = tkinter.Label(window, text="Student ID:", bg="azure", font=("Serif", 10))
student_id_label.place(x=60, y=200)
student_id_entry = tkinter.Entry(window, width=30, bg="white")
student_id_entry.place(x=300, y=200)

gender_label = tkinter.Label(window, text="Gender:", bg="azure", font=("Serif", 10))
gender_label.place(x=60, y=240)
gender_entry = tkinter.Entry(window, width=30, bg="white")
gender_entry.place(x=300, y=240)

age_label = tkinter.Label(window, text="Age:", bg="azure", font=("Serif", 10))
age_label.place(x=60, y=280)
age_entry = tkinter.Entry(window, width=30, bg="white")
age_entry.place(x=300, y=280)

phone_label = tkinter.Label(window, text="Phone Number:", bg="azure", font=("Serif", 10))
phone_label.place(x=60, y=320)
phone_entry = tkinter.Entry(window, width=30, bg="white")
phone_entry.place(x=300, y=320)

level_label = tkinter.Label(window, text="Level:", bg="azure", font=("Serif", 10))
level_label.place(x=60, y=360)
level_entry = tkinter.Entry(window, width=30, bg="white")
level_entry.place(x=300, y=360)


submit_button = tkinter.Button(
    window,
    text="Submit",
    fg="white",
    bg="bisque4",
    font=("Serif", 18, "bold"),
    
)
submit_button.place(x=320, y=500)


window.mainloop()