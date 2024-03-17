# Calculate total holiday cost incl. plane cost, hotel cost, and car-rental cost. (Task 14) Practical Task 1
# written by K.M.Lambert 
# January 2024
# updated February 2024

# Function definitions for calculating costs and total holiday cost
def hotel_cost(num_nights, hotel_choice):
    # Define hotel rates based on choice of city
    hotel_rates = {"Standard": 100, "Double": 150, "Suite": 200}

    # Select the rate based on user's choice, default to Standard if not found
    hotel_rate_per_night = hotel_rates.get(hotel_choice, hotel_rates["Standard"])

    return num_nights * hotel_rate_per_night

def plane_cost(city_flight):
    # Define flight costs based on choices 
    flight_costs = {"Orlando": 500, "Cancun": 700, "Sydney": 1000, "Glasgow": 200}

    # Select the cost based on user's choice, default to 0 if not found
    return flight_costs.get(city_flight, 0)

def car_rental(rental_days, car_choice):
    # Define car rental rates based on choices - can be expanded
    car_rates = {"Small Car": 50, "Medium Car": 75, "SUV": 100}

    # Select the rate based on user's choice, default to Economy if not found
    daily_rental_cost = car_rates.get(car_choice, car_rates["Small Car"])

    return rental_days * daily_rental_cost

def holiday_cost(num_nights, city_flight, hotel_choice, rental_days, car_choice):
    total_hotel_cost = hotel_cost(num_nights, hotel_choice)
    total_plane_cost = plane_cost(city_flight)
    total_car_rental_cost = car_rental(rental_days, car_choice)
    return total_hotel_cost, total_plane_cost, total_car_rental_cost, total_hotel_cost + total_plane_cost + total_car_rental_cost

# Predefined choices for city_flight, hotel, and car rental
city_flight_choices = ["Orlando", "Cancun", "Sydney", "Glasgow"]
hotel_choices = ["Standard", "Double", "Suite"]
car_choices = ["Small Car", "Medium Car", "SUV"]

# Function to get integer input from user with validation
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

# User input for destination
print("City Flight Choices:")
for index, city in enumerate(city_flight_choices, start=1):
    print(f"{index}. {city}")

selected_city_index = get_integer_input("\nEnter the number corresponding to your destination: ")
if 1 <= selected_city_index <= len(city_flight_choices):
    city_flight = city_flight_choices[selected_city_index - 1]
else:
    print("Invalid destination choice. Using default Orlando.")
    city_flight = city_flight_choices[0]

# Get user inputs for other parameters such number of nights
num_nights = get_integer_input("\nEnter the number of nights you will be staying at a hotel: ")
rental_days = get_integer_input("\nEnter the number of days for which you will be hiring a car: ")

# User input for hotel choice
print("\nHotel Choices:")
for index, hotel in enumerate(hotel_choices, start=1):
    print(f"{index}. {hotel}")

selected_hotel_index = get_integer_input("\nEnter the number corresponding to your hotel choice: ")
if 1 <= selected_hotel_index <= len(hotel_choices):
    hotel_choice = hotel_choices[selected_hotel_index - 1]
else:
    print("Invalid hotel choice. Using default Standard.")
    hotel_choice = hotel_choices[0]

# User input for car rental choice
print("\nCar Rental Choices:")
for index, car in enumerate(car_choices, start=1):
    print(f"{index}. {car}")

selected_car_index = get_integer_input("\nEnter the number corresponding to your car rental choice: ")
if 1 <= selected_car_index <= len(car_choices):
    car_choice = car_choices[selected_car_index - 1]
else:
    print("Invalid car rental choice. Using default Small Car.")
    car_choice = car_choices[0]

# Calculate the total holiday cost and breakdown of costs
total_hotel_cost, total_plane_cost, total_car_rental_cost, total_cost = holiday_cost(num_nights, city_flight, hotel_choice, rental_days, car_choice)

# Print holiday details - city, hotel info, car info
print("\nHoliday Details:\n")
print(f"Destination: {city_flight}")
print(f"\nNumber of Nights in Hotel: {num_nights} ({hotel_choice})")
print(f"\nNumber of Days for Car Rental: {rental_days} ({car_choice})")

# Print breakdown of costs
print("\nBreakdown of Costs:\n")
print(f"Hotel Cost: £{total_hotel_cost:.2f}")
print(f"Flight Cost: £{total_plane_cost:.2f}")
print(f"Car Rental Cost: £{total_car_rental_cost:.2f}")

# Print total holiday cost
print(f"\nTotal Holiday Cost: £{total_cost:.2f}\n")
