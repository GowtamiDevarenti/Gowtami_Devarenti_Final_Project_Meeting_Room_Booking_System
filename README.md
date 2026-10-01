# Meeting Room Booking System

A simple **console-based Meeting Room Booking System** developed in Python using Object-Oriented Programming (OOP).

The application allows users to view room availability, create and cancel bookings, view all bookings, and check booking statistics.

## Features

* View meeting room availability
* Create a new room booking
* Prevent double booking of the same room and time slot
* Cancel an existing booking
* View all bookings
* Calculate booking costs automatically
* View booking statistics
* View a summary of bookings for each room
* Validate customer and room information
* Handle invalid user input with error messages

## Room Types

The system supports two types of rooms.

### Meeting Room

Standard meeting rooms have:

* Room ID
* Room name
* Capacity
* Hourly rate

### Conference Room

Conference rooms inherit from `MeetingRoom` and additionally support:

* Projector information
* Equipment fee
* Different cost calculation

Conference rooms have a fixed **€25 equipment fee** added to the hourly rate.

## Available Rooms

The application creates four rooms when it starts:

| Room ID | Room Name         | Type            | Capacity |   Hourly Rate |
| ------- | ----------------- | --------------- | -------: | ------------: |
| 101     | Meeting Room A    | Meeting Room    |        6 |           €40 |
| 102     | Meeting Room B    | Meeting Room    |        8 |           €50 |
| 201     | Conference Room A | Conference Room |       12 | €70 + €25 fee |
| 202     | Conference Room B | Conference Room |       20 | €90 + €25 fee |

## Available Time Slots

The system currently provides three one-hour time slots:

* 09:00 - 10:00
* 10:00 - 11:00
* 11:00 - 12:00

## Project Structure

The project is separated into different modules:

```
meeting-room-booking/
│
├── models.py
├── booking_system.py
├── main.py
└── README.md
```

### `models.py`

Contains the main data models:

* `BookingStatus`
* `Customer`
* `MeetingRoom`
* `ConferenceRoom`
* `Booking`

### `booking_system.py`

Contains the main business logic through the `BookingSystem` class.

It manages:

* Customers
* Rooms
* Bookings
* Room availability
* Booking creation
* Booking cancellation
* Statistics
* Room summaries

### `main.py`

Contains the console user interface.

It provides the main menu and handles user interaction.

## Object-Oriented Programming

This project demonstrates several OOP concepts.

### Encapsulation

Each class contains its own data and related methods.

For example, the `Booking` class contains booking information and methods such as `cancel()` and `conflicts_with()`.

### Inheritance

`ConferenceRoom` inherits from `MeetingRoom`.

```python
class ConferenceRoom(MeetingRoom):
```

This allows the conference room to reuse the functionality of a standard meeting room while adding its own features.

### Polymorphism

Both `MeetingRoom` and `ConferenceRoom` implement:

```
calculate_cost()
```

A normal meeting room returns its hourly rate, while a conference room adds the equipment fee.

This means the booking system can simply call:

```
room.calculate_cost()
```

without needing to know which type of room it is.

### Composition

A `Booking` contains references to a `Customer` and a `MeetingRoom`.

This connects the different objects together to represent a real booking.

### Enum

`BookingStatus` is used to represent the state of a booking:

```
CONFIRMED
CANCELLED
```

Using an enum keeps the booking status consistent throughout the application.

## How the Booking Process Works

The basic booking flow is:

```
Customer enters their details
          ↓
Select a room
          ↓
Select a time slot
          ↓
Check room availability
          ↓
Is the room available?
      ↙           ↘
    No             Yes
    ↓               ↓
Show error      Create booking
                    ↓
             Calculate cost
                    ↓
          Set status to CONFIRMED
                    ↓
             Store booking
```

## Preventing Double Bookings

Before creating a booking, the system checks whether the selected room is already booked for the selected time slot.

If an active booking exists, the system raises an error:

```
This room is already booked for this time slot.
```

Cancelled bookings do not block the time slot.

## Cancelling a Booking

A booking can be cancelled by providing:

* Customer name
* Room ID
* Time slot

The booking is not deleted. Instead, its status changes from:

```
CONFIRMED
```

to:

```
CANCELLED
```

This allows the system to keep a record of cancelled bookings and include them in statistics.

## Booking Statistics

The system provides:

* Total bookings
* Confirmed bookings
* Cancelled bookings
* Confirmed revenue

Revenue is calculated only from confirmed bookings.

## Validation and Error Handling

The application validates user input and raises errors when invalid data is provided.

Examples include:

* Empty customer name
* Invalid email address
* Invalid room ID
* Invalid time slot
* Negative hourly rate
* Invalid room capacity
* Attempting to book an unavailable room
* Attempting to cancel an already cancelled booking

The user interface catches these errors and displays a readable message instead of allowing the application to crash.

## How to Run

### Requirements

* Python 3.10 or newer
* No external packages are required

### Run the application

Open a terminal in the project directory and run:

```
python main.py
```

If your main file has a different name, replace `main.py` with the correct filename.

## Main Menu

When the application starts, the following menu is displayed:

```
==================================================
       MEETING ROOM BOOKING SYSTEM
==================================================
1. Check room availability
2. Create booking
3. Show all bookings
4. Cancel booking
5. Booking statistics
6. Room summary
0. Exit
```

### Menu Options

**1. Check room availability**

Displays the availability of all rooms for each time slot.

**2. Create booking**

Creates a new customer and booking after checking room availability.

**3. Show all bookings**

Displays all bookings and their current status.

**4. Cancel booking**

Cancels an existing confirmed booking.

**5. Booking statistics**

Displays booking totals and confirmed revenue.

**6. Room summary**

Displays booking information for each room.

**0. Exit**

Closes the application.

## Example

A successful booking may look like:

```
Booking #1 | Customer: John Smith |
Room: Meeting Room A |
Room ID: 101 |
Time: 09:00 - 10:00 |
Status: Confirmed |
Cost: €40.00
```

For a conference room, the equipment fee is included automatically.

For example:

```
€70.00 hourly rate + €25.00 equipment fee
= €95.00
```

## Design Highlights

One part of the project I am particularly interested in is the relationship between `MeetingRoom` and `ConferenceRoom`.

`ConferenceRoom` inherits from `MeetingRoom` and overrides the cost calculation:

```
def calculate_cost(self) -> float:
    return self.hourly_rate + self.EQUIPMENT_FEE
```

This demonstrates inheritance and polymorphism while avoiding unnecessary duplicated code.

Another important part is the availability checking. The system checks existing bookings before creating a new booking, which prevents two customers from booking the same room at the same time.

## Possible Future Improvements

The current application could be extended with:

* Multiple booking dates
* More time slots
* Database storage
* User authentication
* Email booking confirmations
* A graphical user interface
* Web-based interface
* More room types
* Different equipment options
* Booking modification
* Search and filtering
* Exporting booking reports

## Conclusion

This project demonstrates how Python and Object-Oriented Programming can be used to build a small but functional booking application.

The main concepts demonstrated are:

* Classes and objects
* Encapsulation
* Inheritance
* Polymorphism
* Composition
* Enums
* Validation
* Exception handling
* Modular programming

The application provides a foundation that can be expanded into a larger meeting room reservation system.

Created as a Python/Object-Oriented Programming project.
