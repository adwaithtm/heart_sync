import tkinter as tk
from tkinter import messagebox
import random

def move_button(event):
    # This makes the "No" button jump to a random spot
    new_x = random.randint(0, window.winfo_width() - no_button.winfo_width())
    new_y = random.randint(0, window.winfo_height() - no_button.winfo_height())
    no_button.place(x=new_x, y=new_y)

def accepted():
    messagebox.showinfo("Success!", "Excellent choice! Date.exe is now running. ❤️")
    window.destroy()

# Setup the window
window = tk.Tk()
window.title("Incoming Request...")
window.geometry("400x300")
window.configure(bg="#ffe6e6")

# The Message
label = tk.Label(window, text="Will you be my valentine?", 
                 font=("Helvetica", 16, "bold"), bg="#ffe6e6", fg="#ff4d6d")
label.pack(pady=50)

# The "Yes" Button
yes_button = tk.Button(window, text="YES", font=("Helvetica", 12), 
                       command=accepted, bg="#ff4d6d", fg="white", width=10)
yes_button.place(x=100, y=150)

# The "No" Button (The prank)
no_button = tk.Button(window, text="NO", font=("Helvetica", 12), width=10)
no_button.place(x=220, y=150)
no_button.bind("<Enter>", move_button) # This triggers when the mouse enters the button area

window.mainloop()
