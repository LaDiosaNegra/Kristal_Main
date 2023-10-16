#user search for hotel by name
class Hotel:
    def __init__(self, hotel_name, location, rooms_available):
        self.hotel_name = hotel_name
        self.location = location
        self.rooms_available = rooms_available

class FiveStarHotel(Hotel):
    def __init__(self, hotel_name, location, rooms_available, price, presidential_suite, executive_suite, deluxe_suite, luxury_suite, standard_suite):
        super().__init__(hotel_name, location, rooms_available)
        self.price = price
        self.presidential_suite = presidential_suite
        self.executive_suite = executive_suite
        self.deluxe_suite = deluxe_suite
        self.luxury_suite = luxury_suite
        self.standard_suite = standard_suite

class FourStarHotel(Hotel):
    def __init__(self, hotel_name, location, rooms_available, price, executive_suite, deluxe_suite, luxury_suite, standard_suite):
        super().__init__(hotel_name, location, rooms_available)
        self.price = price
        self.executive_suite = executive_suite
        self.deluxe_suite = deluxe_suite
        self.luxury_suite = luxury_suite
        self.standard_suite = standard_suite

class ThreeStarHotel(Hotel):
    def __init__(self, hotel_name, location, rooms_available, price, deluxe_suite, luxury_suite, standard_suite):
        super().__init__(hotel_name, location, rooms_available)
        self.price = price
        self.deluxe_suite = deluxe_suite
        self.luxury_suite = luxury_suite
        self.standard_suite = standard_suite



class StarRating:
    def __init__(self, star_rating):
        self.star_rating = star_rating

class User:
    def __init__(self, user_name, email, phone_number):
        self.user_name = user_name
        self.email = email
        self.phone_number = phone_number

class Booking:
    def __init__(self, hotel_name, location, rooms_available, price, presidential_suite, executive_suite, deluxe_suite, luxury_suite, standard_suite):
        self.hotel_name = hotel_name
        self.location = location
        self.rooms_available = rooms_available
        self.price = price
        self.presidential_suite = presidential_suite
        self.executive_suite = executive_suite
        self.deluxe_suite = deluxe_suite
        self.luxury_suite = luxury_suite
        self.standard_suite = standard_suite

# Create objects for the five-star hotels

# Objects

# Five-star hotels
kempinski = FiveStarHotel("Kempinski Hotel Gold Coast City", "Accra", True, 500, True, True, True, True, True)
marriott = FiveStarHotel("Marriott Hotel Accra", "Accra", True, 450, True, True, True, True, True)
movenpick = FiveStarHotel("Mövenpick Ambassador Hotel Accra", "Accra", True, 400, True, True, True, True, True)
labadi_beach_hotel = FiveStarHotel("Labadi Beach Hotel", "Accra", True, 350, True, True, True, True, True)
tang_hotel = FiveStarHotel("Tang Palace Hotel", "Accra", True, 300, True, True, True, True, True)

# Four-star hotels
lancaster_kumasi = FourStarHotel("Lancaster Kumasi City Hotel", "Kumasi", True, 250, True, True, True, True)
lancaster_accra = FourStarHotel("Lancaster Accra City Hotel", "Accra", True, 200, True, True, True, True)
villa_monticello = FourStarHotel("Villa Monticello Hotel", "Accra", True, 150, True, True, True, True)
royal_senchii = FourStarHotel("Royal Senchii", "Akosombo", True, 100, True, True, True, True)
la_palm_royal = FourStarHotel("La Palm Royal Beach Hotel", "Accra", True, 50, True, True, True, True)

# Three-star hotels
zaina = ThreeStarHotel("Zaina Lodge", "Accra", True, 30, True, True, True)
oak_plaza_kumasi = ThreeStarHotel("Oak Plaza Hotel Kumasi", "Kumasi", True, 25, True, True, True)
orchid_hotel = ThreeStarHotel("Orchid Hotel", "Accra", True, 20, True, True, True)
african_regen = ThreeStarHotel("African Regent Hotel", "Accra", True, 15, True, True, True)
the_palms_pram_pram = ThreeStarHotel("The Palms Resort", "Pram Pram", True, 10, True, True, True)


# Create objects for the five-star hotels








# allow user to select a hotel by location (accra, tamale, pram pram, or kumasi) by choosing a number
print("Please select a hotel by location: ")
print("1. Accra")
print("2. Kumasi")
print("3. Tamale")
print("4. Pram Pram")
print("5. Akosombo")

# display list of hotels based on user's location choice
while True:
    try:
        user_location = int(input("Please enter a number: "))
        if user_location < 1 or user_location > 5:
            raise ValueError("Invalid selection. Please enter a number from 1 to 5.")
        break
    except ValueError as e:
        print(e)
        print("Please try again.")
        break

# continue with your code


# define the variable `hotel_name` based on the user's selection
# get the hotel name based on the user's location choice
if user_location == 1:
    print("Please select a hotel in Accra: ")
    print("1. Kempinski Hotel Gold Coast City")
    print("2. Marriott Hotel Accra")
    print("3. Mövenpick Ambassador Hotel Accra")
    print("4. Labadi Beach Hotel")
    print("5. Tang Palace Hotel")

    hotel_choice = None
    while True:
        try:
            hotel_choice = int(input("Please enter a number: "))
            if hotel_choice < 1 or hotel_choice > 5:
                raise ValueError("Invalid selection. Please enter a number from 1 to 5.")
            break
        except ValueError as e:
            print(e)
            print("Please try again.")
            continue

    # try to get the hotel name based on the user's selection
    try:
        if hotel_choice == 1:
            hotel_name = "Kempinski Hotel Gold Coast City"
        elif hotel_choice == 2:
            hotel_name = "Marriott Hotel Accra"
        elif hotel_choice == 3:
            hotel_name = "Mövenpick Ambassador Hotel Accra"
        elif hotel_choice == 4:
            hotel_name = "Labadi Beach Hotel"
        elif hotel_choice == 5:
            hotel_name = "Tang Palace Hotel"
    except (ValueError, TypeError, IndexError) as e:
        print("Invalid input. Please try again.")



    
    
if user_location == 2:
    print("Please select a hotel in Kumasi: ")
    print("1. Lancaster Kumasi City Hotel")
    print("2. Oak Plaza Hotel Kumasi")

    while True:
        try:
            hotel_choice = int(input("Please enter a number: "))
            if hotel_choice < 1 or hotel_choice > 2:
                raise ValueError("Invalid selection. Please enter a number from 1 to 2.")
            break
        except ValueError as e:
            print(e)
            print("Please try again.")

    if hotel_choice == 1:
        hotel_name = "Lancaster Kumasi City Hotel"
    elif hotel_choice == 2:
        hotel_name = "Oak Plaza Hotel Kumasi"

elif user_location == 3:
    print("Please select a hotel in Tamale: ")
    print("1. Zaina Lodge")

    while True:
        try:
            hotel_choice = int(input("Please enter a number: "))
            if hotel_choice < 1 or hotel_choice > 1:
                raise ValueError("Invalid selection. Please enter a number from 1 to 1.")
            break
        except ValueError as e:
            print(e)
            print("Please try again.")


elif user_location == 4:
  # get the hotel name based on the user's selection
  print("Please select a hotel in PramPram: ")
  print("1. The Palms Resort")

  while True:
    try:
      hotel_choice = int(input("Please enter a number: "))
      if hotel_choice < 1 or hotel_choice > 1:
        raise ValueError("Invalid selection. Please enter a number from 1 to 1.")
      break
    except ValueError as e:
      print(e)
      print("Please try again.")

  if hotel_choice == 1:
    hotel_name = "The Palms Resort"

elif user_location == 5:
  # get the hotel name based on the user's selection
  print("Please select a hotel in Akosombo: ")
  print("1. Royal Senchii")

  while True:
    try:
      hotel_choice = int(input("Please enter a number: "))
      break
    except ValueError as e:
      print(e)
      print("Please try again.")

  if hotel_choice == 1:
    hotel_name = "Royal Senchii"
  else:
    print("Invalid hotel selection. Please try again.")

  # Display the list of room types and get the user's selection.
  print("Please select a room type: ")
  print("1. Presidential Suite ($1000 per night)")
  print("2. Executive Suite ($500 per night)")
  print("3. Deluxe Suite ($300 per night)")
  print("4. Luxury Suite ($200 per night)")
  print("5. Standard Suite ($100 per night)")
  print("6. Return to main menu")

  while True:
    try:
      user_room_type = int(input("Please enter a number: "))
      if user_room_type < 1 or user_room_type > 6:
        raise ValueError("Invalid selection. Please enter a number from 1 to 6.")
      break
    except ValueError as e:
      print(e)
      print("Please try again.")

elif user_location == 5:
  # get the hotel name based on the user's selection
  print("Please select a hotel in Akosombo: ")
  print("1. Royal Senchii")

  while True:
    try:
      hotel_choice = int(input("Please enter a number: "))
      break
    except ValueError as e:
      print(e)
      print("Please try again.")

  if hotel_choice == 1:
    hotel_name = "Royal Senchii"
  else:
    print("Invalid hotel selection. Please try again.")

def select_room_type_and_price():
  """Displays a list of room types and allows the user to select a room type by choosing a number. Returns the selected room type with corresponding price.

  Returns:
    A tuple containing the user's selected room type and price.
  """

  # Create a list of room types and prices.
  room_types = ["Presidential Suite", "Executive Suite", "Deluxe Suite", "Luxury Suite", "Standard Suite"]
  room_type_prices = [1000, 500, 300, 200, 100]

  # Display the list of room types and prices to the user.
  print("Please select a room type:")
  for i in range(len(room_types)):
    print("{}. {} (${} per night)".format(i + 1, room_types[i], room_type_prices[i]))

  # Get the user's selection.
  while True:
    try:
      user_selection = int(input("Please enter a number: "))
      if user_selection < 1 or user_selection > len(room_types):
        raise ValueError("Invalid selection. Please enter a number from 1 to {}.".format(len(room_types)))
      break
    except ValueError as e:
      print(e)
      print("Please try again.")

  # Get the room type and price.
  room_type = room_types[user_selection - 1]
  room_type_price = room_type_prices[user_selection - 1]

  return room_type, room_type_price



import datetime

def calculate_total_price(check_in_date, check_out_date, room_type_price):
  """Calculates the total price of a hotel room based on the check-in and check-out dates and the room type price.

  Args:
    check_in_date: A datetime.date object representing the check-in date.
    check_out_date: A datetime.date object representing the check-out date.
    room_type_price: The price of the room type per night.

  Returns:
    The total price of the hotel room.
  """
# Get the check-in and check-out dates from the user.
check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
check_out_date = input("Enter check-out date (YYYY-MM-DD): ")

# Validate the dates.
try:
  check_in_date = datetime.datetime.strptime(check_in_date, "%Y-%m-%d")
  check_out_date = datetime.datetime.strptime(check_out_date, "%Y-%m-%d")
except ValueError:
  print("Invalid date format. Please enter dates in YYYY-MM-DD format.")

# Check if the check-out date is after the check-in date.
if check_out_date > check_in_date:
  # The dates are valid.
  print("The dates are valid.")
else:
  # The check-out date is before the check-in date.
  print("The check-out date must be after the check-in date.")

# Get the user's selection for the room type.
room_type = select_room_type_and_price()

# Calculate the number of nights.
number_of_nights = (check_out_date - check_in_date).days

# Calculate the total price.
total_price = number_of_nights * room_type[1]

# Display the total price to the user.
print("The total price is ${}.".format(total_price))




def get_user_details():
  """Asks the user for their first name, surname, phone number, and email address.

  Returns:
    A tuple containing the user's first name, surname, phone number, and email address.
  """

  # Ask the user for their first name.
  first_name = input("Enter your first name: ")
  first_name = first_name.capitalize()

  # Ask the user for their surname.
  surname = input("Enter your surname: ")
  surname = surname.capitalize()

  # Ask the user for their phone number.
  phone_number = input("Enter your phone number: ")
  phone_number = phone_number.capitalize()

  # Ask the user for their email address.
  email_address = input("Enter your email address: ")
  email_address = email_address.capitalize()

  return first_name, surname, phone_number, email_address

# Get the user's details.
first_name, surname, phone_number, email_address = get_user_details()

# Print the user's details.
print("Your details are:")
print("First name:", first_name)
print("Surname:", surname)
print("Phone number:", phone_number)
print("Email address:", email_address)




import random

def confirm_booking(check_in_date, check_out_date, room_type, total_price, first_name, surname, phone_number, email_address):
  """Asks the user to confirm their booking and prints the booking details with a booking confirmation number, or returns to the main menu or quits if the user says no.

  Args:
    check_in_date: The check-in date.
    check_out_date: The check-out date.
    room_type: The room type.
    total_price: The total price of the booking.
    first_name: The user's first name.
    surname: The user's surname.
    phone_number: The user's phone number.
    email_address: The user's email address.

  Returns:
    A string indicating whether the user wants to continue with the booking,
    return to the main menu, or quit.
  """

  # Ask the user to confirm their booking.
  user_confirmation = input("Do you want to confirm your booking? (yes/no/main/quit): ")

  # If the user confirms their booking, print the booking details with a booking confirmation number.
  if user_confirmation == "yes":
    booking_confirmation_number = random.randint(100000, 999999)
    print("Booking confirmed!")
    print("Booking details:")
    print("Check-in date:", check_in_date)
    print("Check-out date:", check_out_date)
    print("Room type:", room_type)
    print("Total price:", total_price)
    print("Booking confirmation number:", booking_confirmation_number)
    print("User details:")
    print("First name:", first_name)
    print("Surname:", surname)
    print("Phone number:", phone_number)
    print("Email address:", email_address)
    return "continue booking"

  # If the user wants to return to the main menu, return "main menu".
  if user_confirmation == "main":
    return "main menu"

  # If the user wants to quit, return "quit".
  if user_confirmation == "quit":
    return "quit"

  # If the user enters an invalid response, ask them to try again.
  else:
    print("Invalid response. Please enter yes, no, main, or quit.")
    return confirm_booking(check_in_date, check_out_date, room_type, total_price, first_name, surname, phone_number, email_address)



user_choice = confirm_booking(check_in_date, check_out_date, room_type, total_price, first_name, surname, phone_number, email_address)

if user_choice == "continue booking":
  print("Great! Your booking is complete.")
elif user_choice == "main menu":
  print("Returning to the main menu...")
elif user_choice == "quit":
  print("Quitting the program...")
else:
  print("Invalid response.")