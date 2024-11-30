**🚗 Drive-in-Khmer**

An intuitive and user-friendly car rental system designed for Cambodia, offering flexibility, privacy, and customization for short trips.

**📌 Project Overview**

Drive-in-Khmer is an online service aimed at solving car rental challenges in Cambodia. It provides a convenient way for users to rent a car anytime and anywhere. The system emphasizes flexibility, affordability, and personalization to meet user needs.

**📌Problems Addressed:**

	-Lack of car rental systems in Cambodia.

	-Difficulty in renting vehicles for short trips.

	-Limited options for customization and privacy.

**📌Solutions:**

	-🌐 Anywhere, Anytime: Convenient online booking platform.
 
	-💰 Reasonable Prices: Affordable rates for users.
 
	-🛠️ Customization: Options to choose car type, color, seats, and rental duration.
 
	-📆 Short Trips: Designed for both short-term and long-term rentals.
 
	-💳 Online Payment: Seamless payment process using Visa.
 
	-🖥️ Intuitive Interface: Easy navigation for booking, customizing, and payment.
 
**🚀 Current Progress**

1. **Problem Analysis**
Finding a private vehicle for short trips in Cambodia can be challenging. This platform solves the issue by providing an alternative to public transportation, prioritizing user comfort and privacy.

2. **Design**
Using Tkinter GUI, the platform features:

	-A clean, user-friendly interface.
 
	-Simple navigation for customization and transactions.
 
3. **Implementation**

	Key features include:

	-Vehicle customization.
 
	-Online payment options.
 
	-Downloadable receipts.

	-Store information in database.
 

4. **Testing and Debugging**
   
 	-Through testing for smooth transitions and error handling.

	-Database integration for accurate data management.

  	-Debugging the error in each page to make sure a smooth transition when users click on buttons or missing 		information

5. **Development**
The application is in the development phase with planned improvements for:

	-Enhanced UI/UX.

	-Additional features to stand out in the market.

🛠️ Features

User Functions:
🔑 Sign-up/Login:
New users can register by providing username, email, password, and confirmation.
Existing users can log in using their credentials.
📜 Description Page:
Overview of the application with purpose and contact details.
🏠 Homepage:
Vehicle selection with options to customize:
Car type.
Color.
Number of seats.
Rental duration and dates.
Contact information (phone number).
💳 Payment:
Visa card payment with cardholder name, card number, and CVV.
Pre-payment receipt preview for confirmation.
📄 Downloadable Receipt:
Receipt with payment confirmation and booking details.
📋 Expected Pages

Sign-up/Login Page.
Description Page.
Homepage.
Vehicle Database Page.
📂 Database

The system uses SQLite3 and TablePlus for data storage. Key tables include:

Customer_info:
Stores user registration and login details.
Orders_detail:
Tracks user bookings.
Pay_status:
Indicates payment success (1) or failure (0).
Vehicles_info:
Maintains vehicle inventory.
⚙️ Tools and Technologies

Language: Python
Framework: Tkinter
Database: SQLite3
GUI Management: TablePlus
Payment: Visa card integration
📈 Development Status

The application is functional but under continuous improvement. Future updates include:

Enhanced UI design.
Additional payment options (e.g., ABA).
Localization for Khmer users.
