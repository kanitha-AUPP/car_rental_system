# car_rental_system

#Project Title: Drive-in-Khmer
 
**Project Issues and Problem to be solved:** Drive-in-Khmer rental system is an online service to help people get a vehicle for their short-trip. 
**Problem:  **
-Lack of car rental system in Cambodia 
-It is hard to rent a car for a short-time
-Lack of customization 
**Solution: **
-Allow people to rent their car anywhere and anytime
-Reasonable prices
-Able to customize their car (type, colors, seats)
-Able to rent for a short-trip
-Offer online payment
-implement a simple, intuitive interface for browsing cars, selecting vehicles, and completing transactions.

**Current Progress: **

**Problem Analysis:** The problem is relating to the difficulties of finding a car for a short-trip. Most often, people book the bus which also includes other strangers. In this case, they might feel a bit comfortable or lack privacy. If there’s an easy way to access a vehicle where you can have it for your own privacy, it would be great. Therefore, I have an idea of developing a car rental system (Drive-in-Khmer) to help solve these problems. 

**Design:** The design is using Tkinter GUI to create a user-friendly interface where people could understand the function of each button and allow them to customize the vehicle they need. 

**Implementation: **
Develop key features such as vehicle customization, payment method, and downloadable receipt for users. 
Store important information in database

**Testing and Debugging: **
Test the code to see it functionality and improvement
Make sure that needed information is inserted into database 
Debugging the error in each page to make sure a smooth transition when users click on buttons or missing information

**Development: **
The application has an ongoing development of functions and UI to ensure that  it’s user-friendly. The system is not excellent yet it still needs some more improvement to make it stand out from other similar applications. 

**Project function/features: **
**User function: **
-**Sign-up/Login:** Enter the required information like username, email, password, and confirm password. If the user is new, they can sign up. If they already have an account, they can click on the login button. 
-**Description page:** A little brief about the application that includes purposes and contact information. 
-**Homepage:** This page is for users to choose their preferable vehicle and customize the color, seats, duration for renting, rental dates, and enter their phone number for contact. 
Loading receipt for confirmation: before paying, the app allows users to confirm their selection then proceed to pay. 
-**Payment:** The payment is done through the visa card process as the user needs to enter the cardholder name, card number, and CVV. 
-After payment, there’s a downloadable receipt for users to keep it. Everything is done, the app is going to lead you to the description page. 
	
**Expected No. of pages: **
-Sign-up and Login page
-Description page
-Homepage
-Vehicle Database page 

**Database Applied: **
	This application uses SQLite3 and connects to Table Plus for storing the database.
	It includes 4 tables: 
-**Customer_info:** storing the sign-up info. When users want to login if their information is in the database, we lead them in.
-**Orders_detail:** Storing the users booking information. Therefore, after the booking, we can check in the database and send the car to them. 
-**Pay_status:** During the payment, if it’s successful, it stores as 1 in the database. If it’s failed or the user hasn’t paid yet, it stores as 0. 
-**Vehicles_info:** Store the list of vehicles that we have in our shop. 

**Project References:** This application is built from my own knowledge. In some function that I’m not familiar with, I used ChatGPT for help and debugging the code. 

