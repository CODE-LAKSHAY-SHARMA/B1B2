import tkinter as tk
from tkinter import messagebox


def submit_details():
    name = name_entry.get()
    sapid = sapid_entry.get()
    course = course_entry.get()
    phone = phone_entry.get()

    print(f"Name: {name}")
    print(f"SAPID: {sapid}")
    print(f"Course: {course}")
    print(f"Phone: {phone}")

    messagebox.showinfo("Submitted", "Details submitted successfully!")


root = tk.Tk()
root.title("File Organizer")

name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

sapid_label = tk.Label(root, text="SAPID:")
sapid_label.grid(row=1, column=0, padx=10, pady=5)
sapid_entry = tk.Entry(root)
sapid_entry.grid(row=1, column=1, padx=10, pady=5)

course_label = tk.Label(root, text="Course:")
course_label.grid(row=2, column=0, padx=10, pady=5)
course_entry = tk.Entry(root)
course_entry.grid(row=2, column=1, padx=10, pady=5)

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=3, column=0, padx=10, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=3, column=1, padx=10, pady=5)

# Submit button hain
submit_button = tk.Button(root, text="Submit", command=submit_details)
submit_button.grid(row=4, column=1, pady=10)

root.mainloop()
