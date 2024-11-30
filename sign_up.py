import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import _sqlite3

def open_description():
    homepage_path = "/Users/kanithasem/PycharmProjects/pythonProject/Drive-in-Khmer/description.py"
    subprocess.run(["python3", homepage_path])

def custom_alert(message, title="Alert"):
    alert = tk.Toplevel()
    alert.title(title)
    alert.geometry("300x150")
    alert.configure(bg="white")
    alert.resizable(False, False)

    # Message display
    tk.Label(
        alert,
        text=message,
        font=("Arial", 12),
        bg="white",
        wraplength=250
    ).pack(pady=20)

    # OK Button
    tk.Button(
        alert,
        text="OK",
        font=("Arial", 10),
        bg="#3CB3D1",
        fg="black",
        relief="flat",
        command=alert.destroy
    ).pack(pady=10)

    alert.transient(root)
    alert.grab_set()
    alert.wait_window()

def validate_login(email, password):
    # Replace these with actual logic for validating credentials
    conn = _sqlite3.connect('rental.db')
    cursor = conn.cursor()
    global find_email
    find_email = entry_email.get()
    find_password = entry_password.get()
    cursor.execute("SELECT * FROM customer_info WHERE email = ? AND password = ?", (find_email, find_password))
    global result
    result = cursor.fetchone()

    if not find_email or not find_password:
        custom_alert("All fields are required.", "Error")
    elif result is None:
        custom_alert("Your email or password is incorrect.", "Error")
    else:
        custom_alert("Login Successfully.", "Success")
        open_description()



def login_page():
    global entry_email, entry_password
    login_window = tk.Toplevel(root)
    login_window.title("Login Page")
    login_window.geometry("500x600")

    # Frame for the image
    frame_image = tk.Frame(login_window, width=400, height=200, bg="lightgrey")
    frame_image.pack_propagate(False)  # Prevent the frame from resizing with its content
    frame_image.pack(side="top")

    # Load and place the image
    try:
        image = Image.open("/Users/kanithasem/kanitha.txt/images/rental.jpeg")
        photo = ImageTk.PhotoImage(image.resize((400, 200)))

        label_image = tk.Label(frame_image, image=photo, bg="lightgrey")
        label_image.image = photo  # Keep a reference to the image
        label_image.pack(fill="both", expand=True)
    except FileNotFoundError:
        tk.Label(frame_image, text="Image not found!", bg="lightgrey", font=("Arial", 12)).pack()

    # Frame for the form
    frame_form = tk.Frame(login_window, bg="#cce5ff", padx=20, pady=20, relief="ridge", bd=2)
    frame_form.pack(fill="both", expand=True, padx=20, pady=10)

    tk.Label(frame_form, text="Login", font=("Arial", 24, "bold"), bg="#cce5ff").pack(pady=10)

    tk.Label(frame_form, text="Email:", font=("Arial", 12), bg="#cce5ff").pack(anchor="w", padx=20, pady=5)
    entry_email = tk.Entry(frame_form, font=("Arial", 12), width=30)
    entry_email.pack(fill='x', pady=5)

    tk.Label(frame_form, text="Password:", font=("Arial", 12), bg="#cce5ff").pack(anchor="w", padx=20, pady=5)
    entry_password = tk.Entry(frame_form, font=("Arial", 12), width=30, show="*")
    entry_password.pack(fill='x', pady=5)

    login_button = tk.Button(
    frame_form,
    text="Login",
    font=("Arial", 12, "bold"),
    bg="#3CB3D1",
    fg="black",
    relief="flat",
    command=lambda: validate_login(entry_email, entry_password))
    login_button.pack(pady=20)

    # Run the Tkinter event loop
    login_window.mainloop()
def database_sign_up():
    conn = _sqlite3.connect('rental.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS customer_info(
                    id INTEGER PRIMARY KEY,
                    username TEXT,
                    email TEXT,
                    password INTEGER
                    )''')
    username = entry_name_signup.get()
    email = entry_email_signup.get()
    password = entry_password_signup.get()
    cursor.execute(
        f"INSERT INTO customer_info(username, email, password) VALUES ('{username}', '{email}', '{password}')")
    conn.commit()
    open_description()
def GUI():
    global entry_name_signup, entry_email_signup, entry_password_signup, root
    root = tk.Tk()
    root.title("Sign-Up Form")
    root.geometry("500x800")

    # Create a frame for the image
    frame_image = tk.Frame(root, width=400, height=200, bg="lightgrey")
    frame_image.pack_propagate(False)  # Prevent the frame from resizing with its content
    frame_image.pack(side="top")

    # Load and place the image
    image = Image.open("/Users/kanithasem/kanitha.txt/images/rental.jpeg")  # Update with the correct path
    photo = ImageTk.PhotoImage(image.resize((400, 200)))  # Resize the image
    label_image = tk.Label(frame_image, image=photo, bg="lightgrey")
    label_image.pack(fill="both", expand=True)

    # Create a frame for the sign-in form
    frame_form = tk.Frame(root, bg="#cce5ff", padx=20, pady=20, relief="ridge", bd=2)
    frame_form.pack(fill="both", expand=True, padx=20, pady=10)

    label_title = tk.Label(frame_form, text="Welcome To", font=("Arial", 30, "bold"), bg="#cce5ff", fg="#333")
    label_title.pack(pady=10)

    label_title = tk.Label(frame_form, text="Drive-in-Khmer", font=("Arial", 36, "italic"), bg="#cce5ff", fg="#333")
    label_title.pack(pady=10)

    # Add form title
    label_form_title = tk.Label(frame_form, text="Sign Up", font=("Arial", 16, "bold"), bg="#cce5ff", fg="#333")
    label_form_title.pack(pady=10)

    # Name field
    label_name = tk.Label(frame_form, text="Name:", font=("Arial", 12), bg="#cce5ff", anchor="w")
    label_name.pack(fill="x")
    entry_name_signup = tk.Entry(frame_form, font=("Arial", 12), bg="#f1f1f1", relief="solid")
    entry_name_signup.pack(fill="x", pady=5)

    # Email field
    label_email = tk.Label(frame_form, text="Email:", font=("Arial", 12), bg="#cce5ff", anchor="w")
    label_email.pack(fill="x")
    entry_email_signup = tk.Entry(frame_form, font=("Arial", 12), bg="#f1f1f1", relief="solid")
    entry_email_signup.pack(fill="x", pady=5)

    #     # Password field
    label_password = tk.Label(frame_form, text="Password:", font=("Arial", 12), bg="#cce5ff", anchor="w")
    label_password.pack(fill="x")
    entry_password_signup = tk.Entry(frame_form, show="*", font=("Arial", 12), bg="#f1f1f1", relief="solid")
    entry_password_signup.pack(fill="x", pady=5)

    #     # Confirm Password field
    label_confirm_password = tk.Label(frame_form, text="Confirm Password:", font=("Arial", 12), bg="#cce5ff", anchor="w")
    label_confirm_password.pack(fill="x")
    entry_confirm_password_signup = tk.Entry(frame_form, show="*", font=("Arial", 12), bg="#f1f1f1", relief="solid")
    entry_confirm_password_signup.pack(fill="x", pady=5)

    #     # Submit button
    button_submit = tk.Button(frame_form, text="Sign-Up", font=("Arial", 12, "bold"), bg="#3CB3D1", fg="#000000",
                              activebackground="#3CB3D1", relief="flat", command=database_sign_up)
    button_submit.pack(pady=10)

    button_submit = tk.Button(frame_form, text="Login", font=("Arial", 12, "bold"), bg="#3CB3D1", fg="#000000",
                              activebackground="#3CB3D1", relief="flat", command=login_page)
    button_submit.pack(pady=10)

    root.mainloop()
GUI()
