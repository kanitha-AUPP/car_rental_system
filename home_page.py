import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import Calendar
from fpdf import FPDF
from tkinter import Toplevel, filedialog
import _sqlite3
import subprocess

class CarRental:
    def __init__(self, root, car_name, image_path, price_per_day):
        self.root = root
        self.car_name = car_name
        self.image_path = image_path
        self.price_per_day = price_per_day

        self.root.geometry("800x1100")

        # Variables
        self.color_var = tk.StringVar(value=" ")
        self.seat_var = tk.StringVar(value=" ")
        self.day_var = tk.StringVar(value=" ")
        self.selected_date = None
        self.status = True

        self.seat_options = {
            "Sedan": ["4 seats", "5 seats"],
            "SUV": ["5 seats", "7 seats", "8 seats"],
            "Pickup_truck": ["2 seats", "4 seats", "6 seats"],
            "Convertible": ["2 seats", "4 seats"],
            "Hatchback": ["4 seats", "5 seats"]
        }

        self.car_choice()

    def car_choice(self):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Title
        label_title = tk.Label(self.root, text=f"{self.car_name} Vehicle Type", font=("Arial", 30, "bold"), bg="#cce5ff", fg="#333")
        label_title.pack(pady=10)

        # Load and display the image
        image = Image.open(self.image_path)
        photo = ImageTk.PhotoImage(image.resize((200, 100)))
        label_image = tk.Label(self.root, image=photo, bg="#cce5ff")
        label_image.photo = photo  # Keep a reference
        label_image.pack()

        # Car color

        label_color = tk.Label(self.root, text="Car Color: ", font=("Arial", 20, "bold"), bg="#cce5ff", fg="#333")
        label_color.pack(pady=5)

        colors = ["Red", "Blue", "Black", "White"]
        for color in colors:
            tk.Radiobutton(self.root, text=color, variable=self.color_var, value=color, font=("Arial", 15), bg="white").pack()

        # Seat selection
        label_seats = tk.Label(self.root, text="The Amount of Seats: ", font=("Arial", 20, "bold"), bg="#cce5ff", fg="#333")
        label_seats.pack(pady=5)

        for seat in self.seat_options.get(self.car_name, []):
            tk.Radiobutton(self.root, text=seat, variable=self.seat_var, value=seat, font=("Arial", 15), bg="white").pack()

        # Rental duration
        label_days = tk.Label(self.root, text="Duration for Renting: ", font=("Arial", 20, "bold"), bg="#cce5ff", fg="#333")
        label_days.pack(pady=5)

        days = [5, 7]
        for day in days:
            tk.Radiobutton(self.root, text=f"{day} days", variable=self.day_var, value=str(day), font=("Arial", 15), bg="white").pack()

        # Rental date
        label_date = tk.Label(self.root, text="Select your rental date:", font=("Arial", 20, "bold"), bg="#cce5ff", fg="#333")
        label_date.pack(pady=5)

        self.calendar = Calendar(
                        self.root,
                        selectmode="day",
                        background="white",
                        disabledbackground="gray",
                        bordercolor="black",
                        headersbackground="lightblue",
                        normalbackground="white",
                        foreground="black",
                        weekendbackground="lightgray",
                        weekendforeground="black",
                        selectbackground="lightblue",
                        selectforeground="red",
                        showweeknumbers=False
                    )
        self.calendar.pack(pady=5)

        global entry_number
        entry_number = tk.Label(self.root, text="Enter Your Phone Number", font=("Arial", 20, "bold"), bg="#cce5ff",
                                fg="#333")
        entry_number.pack(pady=5)
        entry_number = tk.Entry(self.root, font=("Arial", 12), width=30)
        entry_number.pack(pady=5)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        select_button = tk.Button(button_frame, text="Submit", font=("Arial", 12, "bold"), command=self.validate_selection, bg="#4CAF50", fg="black")
        select_button.pack(side="left", padx=5)
        back_button = tk.Button(button_frame, text="Back", font=("Arial", 12, "bold"), command=lambda: open_description(), bg="#4CAF50", fg="black")
        back_button.pack(side="right",padx=5)


    def validate_selection(self):
        # Initialize a list to store missing fields
        missing_fields = []

        # Check for missing inputs and append the corresponding field names to the list
        if not self.color_var.get():
            missing_fields.append("Car Color")
        if not self.seat_var.get():
            missing_fields.append("Number of Seats")
        if not self.day_var.get():
            missing_fields.append("Rental Duration")
        if not self.calendar.get_date():
            missing_fields.append("Rental Date")
        if not entry_number.get():
            missing_fields.append("Phone Number")

        # If there are missing fields, show an error message
        if missing_fields:
            # Join the missing field names with commas for the message
            missing_fields_text = ", ".join(missing_fields)
            messagebox.showerror("Missing Information", f"Please fill out the information.")
            return

        # If all inputs are valid, proceed
        self.show_info()
        # If all inputs are valid, proceed

    def show_info(self):
        car_color = self.color_var.get()
        seats = self.seat_var.get()
        duration = self.day_var.get()
        self.selected_date = self.calendar.get_date()

        if not car_color or not seats or not duration or not self.selected_date:
            tk.messagebox.showerror("Missing Information", "Please fill out all fields!")
            return
        else:
        #database
            conn = _sqlite3.connect('rental.db')
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS orders_detail(
                                                   id INTEGER PRIMARY KEY,
                                                   phone TEXT,
                                                   car TEXT,
                                                   color TEXT,
                                                   seat TEXT,
                                                   duration INTEGER
                                                   )''')
            global phone
            phone = entry_number.get()
            cursor.execute('''INSERT INTO orders_detail(phone, car, color, seat, duration) VALUES (?, ?, ?, ?, ?)''',
                               (phone, self.car_name, car_color , seats, duration))

            conn.commit()

            cursor.execute("DROP TABLE IF EXISTS order_info")
            cursor.execute("DROP TABLE IF EXISTS orders_info")
            cursor.execute("DROP TABLE IF EXISTS orders_table")




        # Open the custom confirmation box
            self.show_confirmation_box(car_color, seats, duration, self.selected_date)

    def show_confirmation_box(self, car_color, seats, duration, selected_date):
            # Create the confirmation window
            confirm_window = tk.Toplevel(self.root)
            confirm_window.title("Confirm Reservation")
            confirm_window.geometry("300x200")
            confirm_window.resizable(False, False)

            # Display reservation details
            tk.Label(confirm_window, text="Confirm Your Reservation", font=("Arial", 14, "bold")).pack(pady=10)
            tk.Label(
                confirm_window,
                text=f"Car: {self.car_name}\nColor: {car_color}\nSeats: {seats}\nDuration: {duration} days\nDate: {selected_date}",
                font=("Arial", 12),
                justify="left"
            ).pack(pady=10)

            def confirm_yes():
                return self.generate_receipt(car_color, seats, duration)
            def confirm_no():
                return self.car_choice()

            tk.Button(confirm_window, text="Yes", command=lambda:[self.generate_receipt(car_color, seats, duration),
                                                                    confirm_window.destroy()]).pack(side="left", padx=20)
            tk.Button(confirm_window, text="No", command=confirm_window.destroy).pack(side="right", padx=20)


    def generate_receipt(self, car_color, seats, duration):
            rental_cost = int(duration) * self.price_per_day

            # Create a new window for the receipt
            receipt_window = Toplevel()
            receipt_window.title("Rental Receipt")
            receipt_window.geometry("400x300")
            receipt_window.resizable(False, False)

            # Add a title to the receipt
            title_label = tk.Label(receipt_window, text="Drive-in-Khmer", font=("Arial", 16, "bold"))
            title_label.pack(pady=5)

            title_label = tk.Label(receipt_window, text="Car Rental Receipt", font=("Arial", 14, "bold"))
            title_label.pack(pady=5)

            receipt_width = 90
            # Add receipt details
            receipt_text = (
                f"{'-' * receipt_width}\n"
                f"{f'Car Model: {self.car_name}'.center(receipt_width)}\n"
                f"{f'Car Color: {car_color}'.center(receipt_width)}\n"
                f"{f'Seats: {seats}'.center(receipt_width)}\n"
                f"{f'Rental Start: {self.selected_date}'.center(receipt_width)}\n"
                f"{f'Duration: {duration} days'.center(receipt_width)}\n"
                f"{f'Price per Day: ${self.price_per_day}'.center(receipt_width)}\n"
                f"{f'Total Cost: ${rental_cost}'.center(receipt_width)}\n"
                f"{'-' * receipt_width}\n"
                f"{f'Please return the car back in {duration} days.'.center(receipt_width)}\n"
                f"{'Enjoy Your Trip!!'.center(receipt_width)}"
            )

            receipt_label = tk.Label(receipt_window, text=receipt_text, font=("Arial", 12), justify="left", anchor="w")
            receipt_label.pack(pady=10, padx=20, anchor="w")

            # Add a close button
            close_button = tk.Button(receipt_window, text="PayNow", command=self.process_payment)
            close_button.pack(pady=10)

    def process_payment(self):
        payment_window = Toplevel(self.root)
        payment_window.title("Visa Payment")
        payment_window.geometry("800x700")
        payment_window.resizable(False, False)
        # Frame for the image
        frame_image = tk.Frame(payment_window, width=400, height=200, bg="lightgrey")
        frame_image.pack_propagate(False)  # Prevent the frame from resizing with its content
        frame_image.pack(side="top")

        # Load and display the image
        image_path = "/Users/kanithasem/kanitha.txt/images/visa.png"  # Ensure this is the correct path
        try:
            image = Image.open(image_path)
            resized_image = image.resize((400, 200))  # Resize the image
            photo = ImageTk.PhotoImage(resized_image)  # Create a PhotoImage object
            label_image = tk.Label(frame_image, image=photo, bg="lightgrey")
            label_image.image = photo  # Keep a reference to avoid garbage collection
            label_image.pack(fill="both", expand=True)
        except Exception:
            label_image = tk.Label(frame_image, text="Visa Logo Not Found", bg="lightgrey", fg="red")
            label_image.pack(fill="both", expand=True)

        frame_form = tk.Frame(payment_window, bg="#cce5ff", padx=20, pady=20, relief="ridge", bd=2)
        frame_form.pack(fill="both", expand=True, padx=20, pady=10)

        # Input fields
        tk.Label(frame_form, text="Cardholder Name:", font=("Arial", 16, "bold"), bg="#cce5ff").pack(pady=10)
        entry_name = tk.Entry(frame_form, font=("Arial", 12), width=30)
        entry_name.pack(pady=5)

        tk.Label(frame_form, text="Card Number:", font=("Arial", 16, "bold"), bg="#cce5ff").pack(pady=10)
        entry_card_number = tk.Entry(frame_form, font=("Arial", 12), width=30)
        entry_card_number.pack(pady=5)

        tk.Label(frame_form, text="Expiry Date (MM/YY):", font=("Arial", 16, "bold"), bg="#cce5ff").pack(pady=10)
        entry_expiry = tk.Entry(frame_form, font=("Arial", 12), width=30)
        entry_expiry.pack(pady=5)

        tk.Label(frame_form, text="CVV:", font=("Arial", 16, "bold"), bg="#cce5ff").pack(pady=10)
        entry_cvv = tk.Entry(frame_form, font=("Arial", 12), width=30, show="*")
        entry_cvv.pack(pady=5)

        # Status label
        status_label = tk.Label(frame_form, text="", font=("Arial", 12), bg="#cce5ff")
        status_label.pack(pady=10)

        # Submit button
        btn_submit = tk.Button(frame_form, text="Submit Payment", font=("Arial", 12), bg="#4CAF50", fg="black", command=self.pay_status_info)
        btn_submit.pack(pady=20)

        # Start the Tkinter event loop
        # root.mainloop()
        Toplevel.mainloop(self.root)

        """Handles payment validation and updates the status label."""
        name = entry_name.get()
        card_number = entry_card_number.get()
        expiry_date = entry_expiry.get()
        cvv = entry_cvv.get()

        # Clear the status label before validation
        status_label.config(text="", fg="red")

        if not (name and card_number and expiry_date and cvv):
            status_label.config(text="All fields are required!", fg="red")
            return

        if len(card_number) != 16 or not card_number.isdigit():
            status_label.config(text="Invalid card number. It must be 16 digits.", fg="red")
            return

        if len(cvv) != 3 or not cvv.isdigit():
            status_label.config(text="Invalid CVV. It must be 3 digits.", fg="red")
            return

        # If everything is valid, process the payment and generate a receipt
        if status_label.config(text="Payment processed successfully!", fg="green"):
            self.status = True
        else:
            self.status = False

    def pay_status_info(self):
        conn = _sqlite3.connect('rental.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS pay_status(
                                                           id INTEGER PRIMARY KEY,
                                                           phone TEXT,
                                                           status TEXT
                                                           )''')
        cursor.execute('''INSERT INTO pay_status (phone, status) VALUES (?,?)''', (phone, self.status))
        conn.commit()
        download_receipt(self)

def download_receipt(self):
        # Create the PDF file for the receipt
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        rental_cost = int(self.day_var.get()) * self.price_per_day
        receipt_width = 90
        # Add receipt details
        receipt_text = (
            f"{'Car Rental Receipt'.center(receipt_width)}"
            f"{'-' * receipt_width}\n"
            f"{f'Car Model: {self.car_name}'.center(receipt_width)}\n"
            f"{f'Car Color: {self.color_var.get()}'.center(receipt_width)}\n"
            f"{f'Seats: {self.seat_var.get()}'.center(receipt_width)}\n"
            f"{f'Rental Start: {self.selected_date}'.center(receipt_width)}\n"
            f"{f'Duration: {self.day_var.get()} days'.center(receipt_width)}\n"
            f"{f'Price per Day: ${self.price_per_day}'.center(receipt_width)}\n"
            f"{f'Total Cost: ${rental_cost}'.center(receipt_width)}\n"
            f"{'-' * receipt_width}\n"
            f"{f'Please return the car back in {self.day_var.get()} days.'.center(receipt_width)}\n"
            f"{'Enjoy Your Trip!!'.center(receipt_width)}"
        )

        pdf.multi_cell(0, 10, receipt_text)
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            pdf.output(file_path)
            messagebox.showinfo("Success", "Successfully Paid.")
            open_description()

def open_description():
        homepage_path = "/Users/kanithasem/PycharmProjects/pythonProject/Drive-in-Khmer/description.py"
        subprocess.run(["python3", homepage_path])

def display_cars():
    root = tk.Tk()
    root.title("Car Rental Service")
    root.geometry("700x600")
    root.configure(bg="white")


    header_label = tk.Label(root, text="Welcome to Drive-in-Khmer", font=("Arial", 20), bg="white", fg="black")
    header_label.pack(fill="x", pady=10)

    header_label = tk.Label(root, text='"Enjoy the Best Vehicle for Your Trip."', font=("Times New Roman", 16, "bold"),
                            bg="white", fg="black")
    header_label.pack(fill="x", pady=10)

    frame = tk.Frame(root, bg="white")
    frame.pack(pady=20, fill="both", expand=True)



    car_images = {
                "Sedan": ("/Users/kanithasem/kanitha.txt/images/sedan.webp", 30),
                "SUV": ("/Users/kanithasem/kanitha.txt/images/SUV.jpeg", 40),
                "Pickup_truck": ("/Users/kanithasem/kanitha.txt/images/pickup.webp", 50),
                "Hatchback": ("/Users/kanithasem/kanitha.txt/images/hatchback.jpeg", 20),
                "Convertible": ("/Users/kanithasem/kanitha.txt/images/convertible.webp", 30)
            }

    row, col = 0, 0
    for car, (img_path, price_per_day) in car_images.items():
        img = Image.open(img_path).resize((150, 100))
        photo = ImageTk.PhotoImage(img)

        img_label = tk.Label(frame, image=photo, bg="white")
        img_label.image = photo
        img_label.grid(row=row, column=col, padx=20, pady=20)

        text_label = tk.Label(frame, text=car, bg="white", font=("Arial", 12))
        text_label.grid(row=row + 1, column=col, padx=10, pady=5)

        button = tk.Button(
            frame,
            text=f"Select {car} (${price_per_day}/day)",
            bg="lightblue",
            font=("Arial", 10),
            command=lambda c=car, p=price_per_day, img=img_path: CarRental(root, c, img, p)
        )
        button.grid(row=row + 2, column=col, padx=10, pady=5)

        col += 1
        if col > 2:  # Adjust columns
            col = 0
            row += 3

    select_button = tk.Button(root, text="back", font=("Arial", 12, "bold"), command=open_description,
                              bg="#4CAF50", relief="flat", fg="black")
    select_button.pack(padx=5, pady=10)

    root.mainloop()

display_cars()






