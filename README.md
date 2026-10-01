# Gowtami_Devarenti_Final_Project_Meeting_Room_Booking_System


# Meeting Room Booking System

"""A simple **Python-based Meeting Room Booking System** developed using Object-Oriented Programming (OOP).

The system allows users to view meeting rooms, create bookings, check room availability, view existing bookings, and cancel bookings."""

## Main functionality

* View available meeting rooms
* Display room capacity and hourly rates
* Create a new meeting room booking
* Check room availability before booking
* Store customer information
* View existing bookings
* Cancel bookings
* Calculate booking costs
* Support different types of meeting rooms
* Use booking statuses such as **Confirmed** and **Cancelled**

## Project Structure

```text
Meeting-Room-Booking-System/
│
├── main.py
├── booking_system.py
├── models.py
└── README.md
```

### `main.py`

The main entry point of the application.

It is responsible for:

* Displaying the menu
* Getting input from the user
* Calling the appropriate functions
* Running the booking system

### `booking_system.py`

Contains the main business logic of the application.

It handles:

* Creating bookings
* Checking room availability
* Managing customers
* Managing rooms
* Managing bookings
* Cancelling bookings
* Calculating booking costs

### `models.py`

Contains the main classes used in the application:

* `Customer`
* `MeetingRoom`
* `ConferenceRoom`
* `Booking`
* `BookingStatus`

## Object-Oriented Programming Concepts

This project demonstrates several important OOP concepts.

### Encapsulation

The classes keep related data and functionality together.

For example, customer information is handled inside the `Customer` class and room information is handled inside the room classes.

### Inheritance

`ConferenceRoom` inherits from `MeetingRoom`.

This allows the conference room to reuse functionality from the parent class while adding its own features.

### Polymorphism

Different room types can have their own implementation of the `calculate_cost()` method.

This allows the system to calculate costs differently depending on the type of room.

### Classes and Objects

The system uses classes to represent real-world entities such as:

* Customers
* Meeting rooms
* Conference rooms
* Bookings

Objects are then created from these classes when the program is running.

## How the Booking Process Works

The booking process follows these steps:

1. User selects a meeting room.
2. User selects a time slot.
3. The system checks whether the time slot is valid.
4. The system checks whether the room is available.
5. Customer information is created.
6. A booking is created.
7. The booking is stored in the system.
8. The booking cost is calculated.

## Example

A typical booking flow looks like:

```text
Select a room
      ↓
Select a time slot
      ↓
Check availability
      ↓
Enter customer information
      ↓
Create booking
      ↓
Calculate cost
      ↓
Booking confirmed
```

## How to Run the Project

Make sure Python is installed on your computer.

Clone the repository:

```bash
git clone <your-github-repository-url>
```

Navigate to the project folder:

```bash
cd Meeting-Room-Booking-System
```

Run the program:

```bash
python main.py
```

## Technologies Used

* Python
* Object-Oriented Programming
* Python Enum
* Dictionaries
* Lists
* Functions and Classes

## What I Learned

Through this project, I practiced:

* Designing classes and objects
* Using inheritance and polymorphism
* Organizing code into multiple files
* Separating user interface from business logic
* Validating user input
* Managing bookings and room availability
* Working with relationships between different objects

## Future Improvements

Some possible improvements for the future are:

* Add a database for persistent data storage
* Add dates and booking durations
* Add stronger email validation
* Add automated tests
* Generate unique booking IDs
* Improve the user interface
* Use `Decimal` for more accurate money calculations

## Author

Created as a Python/Object-Oriented Programming project.
