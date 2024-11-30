import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import subprocess


# Function to open another script (Sign Up Page)
def homepage():
    homepage_path = "/Users/kanithasem/PycharmProjects/pythonProject/Drive-in-Khmer/home_page.py"
    subprocess.run(["python3", homepage_path])

# Create the main window
root = tk.Tk()
root.title("Car Rental System")
root.geometry("600x800")  # Adjusted for better responsiveness
root.configure(bg="#f7f7f7")  # Set background color

# Header Section
header_label = tk.Label(
    root,
    text="Welcome to Drive-in-Khmer Rentals!",
    font=("Arial", 28, "bold"),
    fg="darkblue",
    bg="#f7f7f7"
)
header_label.pack(pady=20)

# Image Section
try:
    image = Image.open("/Users/kanithasem/kanitha.txt/images/rental.jpeg")  # Update with correct path
    photo = ImageTk.PhotoImage(image.resize((500, 250)))  # Resize the image
    image_frame = tk.Frame(root, bg="#f7f7f7")
    image_frame.pack(pady=10)
    label_image = tk.Label(image_frame, image=photo, bg="#f7f7f7")
    label_image.pack()
except Exception as e:
    label_image = tk.Label(
        root,
        text="Image not found!",
        font=("Arial", 12, "italic"),
        fg="red",
        bg="#f7f7f7"
    )
    label_image.pack(pady=10)

# Description Section
frame_form = tk.Frame(root, bg="#cce5ff", padx=20, pady=20, relief="ridge", bd=2)
frame_form.pack(fill="both", expand=True, padx=30, pady=10)

label_title = tk.Label(frame_form, text="About Us", font=("Arial", 30, "bold"), bg="#cce5ff", fg="#333")
label_title.pack(pady=10)

description_label = tk.Label(
    frame_form,
    text=(
        "Drive-in-Khmer Rentals offers you the best car rental experience.\n"
        "Choose from a variety of vehicles to suit your needs, whether\n"
        "it's for a weekend getaway, business trip, or daily commute.\n"
        "Book your car today and drive with ease!"
    ),
    font=("Arial", 14),
    bg="#cce5ff",
    justify="center",
    wraplength=600
)
description_label.pack(pady=10)

features_label = tk.Label(
    frame_form,
    text=(
        "* Our Features Include:\n"
        "  - Easy Payment Options\n"
        "  - Customize Your Own Car\n"
        "  - Rent Anytime, Anywhere\n"
    ),
    font=("Arial", 14),
    bg="#cce5ff",
    justify="left",
    anchor="w",
    wraplength=600
)
features_label.pack(pady=10)

# Buttons Section
button_frame = tk.Frame(frame_form, bg="#cce5ff")
button_frame.pack(pady=10)

def on_enter(event):
    event.widget.config(bg="deepskyblue")

def on_leave(event):
    event.widget.config(bg="lightblue")

sign_up_button = tk.Button(
    button_frame,
    text="Get Start",
    font=("Arial", 14),
    bg="lightblue",
    command=homepage,
    width=15
)
sign_up_button.grid(row=0, column=0, padx=10)

sign_up_button.bind("<Enter>", on_enter)
sign_up_button.bind("<Leave>", on_leave)

# Footer Section
footer_label = tk.Label(
    root,
    text="Drive-in-Khmer Rentals © 2024/ Tel: +85589888981 Email: drive_in_khmer@gmail.com",
    font=("Arial", 12, "italic"),
    fg="white",
    bg="darkblue"
)
footer_label.pack(fill="x", pady=10)

# Run the Tkinter event loop
root.mainloop()

