import _sqlite3
conn = _sqlite3.connect('rental.db')
cursor = conn.cursor()
def vehicle_info():

    # Create the table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS vehicles_info(
                        id INTEGER PRIMARY KEY,
                        cars TEXT,
                        colors TEXT,
                        seats TEXT
                        )''')
    cars = ["Sedan", "SUV", "Hatchback", "Convertible", "Pickup_truck"]
    car_colors = ["White", "Black", "Red", "Blue"]
    car_seats = {
        "Sedan": ["4 seats", "5 seats"],
        "SUV": ["5 seats", "7 seats" , "8 seats"],
        "Pickup_truck": ["2 seats", "4 seats", "6 seats"],
        "Convertible": ["2 seats", "4 seats"],
        "Hatchback": ["4 seats", "5 seats"]
    }

    # Insert data into the table
    for car in cars:
        for color in car_colors:
            for seat_option in car_seats.get(car, []):
                cursor.execute('''INSERT INTO vehicles_info(cars, colors, seats) 
                                      VALUES (?, ?, ?)''', (car, color, seat_option))
        # Commit changes and close the connection
    conn.commit()
vehicle_info()

cursor.execute("DROP TABLE IF EXISTS vehicle_info_new")
cursor.execute('DROP TABLE IF EXISTS vehicles')
cursor.execute('DROP TABLE IF EXISTS vehicle_info')