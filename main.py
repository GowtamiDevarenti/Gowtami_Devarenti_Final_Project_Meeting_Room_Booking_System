from booking_system import BookingSystem
from models import BookingStatus


def show_room_availability(
    system: BookingSystem,
) -> None:
    """Show every room with the status of each time slot."""

    print("\n--- ROOM AVAILABILITY ---")

    for room in system.rooms.values():

        print("\n" + "=" * 60)
        print(room)
        print("=" * 60)

        for time_slot in system.TIME_SLOTS:

            if system.is_room_available(
                room,
                time_slot,
            ):
                status = "Available"
            else:
                status = "Booked"

            print(
                f"{time_slot} : {status}"
            )


def choose_time_slot(
    system: BookingSystem,
    room_id: int,
) -> str | None:
    """Show time slots and allow the user to select an available slot."""

    room = system.get_room(room_id)

    print(
        f"\nTime Slots for {room.name}:"
    )

    for number, time_slot in enumerate(
        system.TIME_SLOTS,
        start=1,
    ):

        if system.is_room_available(
            room,
            time_slot,
        ):
            status = "Available"
        else:
            status = "Booked"

        print(
            f"{number}. {time_slot} - {status}"
        )

    choice = input(
        "\nSelect time slot: "
    )

    if not choice.isdigit():
        print("Please enter a number.")
        return None

    slot_number = int(choice)

    if (
        slot_number < 1
        or slot_number > len(system.TIME_SLOTS)
    ):
        print("Invalid time slot.")
        return None

    selected_slot = system.TIME_SLOTS[
        slot_number - 1
    ]

    if not system.is_room_available(
        room,
        selected_slot,
    ):
        print(
            "\nThis time slot is already booked."
        )
        return None

    return selected_slot


def create_booking(
    system: BookingSystem,
) -> None:
    """Ask for customer details and create a booking."""

    print("\n--- CREATE BOOKING ---")

    name = input("Customer name: ")
    email = input("Customer email: ")

    print("\nAvailable Rooms:")

    for room in system.rooms.values():
        print(room)

    try:
        room_id = int(
            input("\nEnter Room ID: ")
        )

        room = system.get_room(room_id)

        time_slot = choose_time_slot(
            system,
            room_id,
        )

        if time_slot is None:
            return

        booking = system.create_booking(
            name,
            email,
            room_id,
            time_slot,
        )

        print(
            "\nBooking created successfully!"
        )
        print(booking)

    except ValueError as error:
        print(f"\nError: {error}")


def show_all_bookings(
    system: BookingSystem,
) -> None:
    """Show all bookings."""

    print("\n--- ALL BOOKINGS ---")

    if not system.bookings:
        print("No bookings found.")
        return

    for booking in system.bookings.values():

        print("\n" + "-" * 60)
        print(f"Booking ID: {booking.booking_id}")
        print(f"Customer: {booking.customer.name}")
        print(f"Email: {booking.customer.email}")
        print(f"Room: {booking.room.name}")
        print(f"Room ID: {booking.room.room_id}")
        print(f"Time: {booking.time_slot}")
        print(f"Status: {booking.status.value}")
        print(f"Cost: €{booking.cost:.2f}")


def cancel_booking(
    system: BookingSystem,
) -> None:
    """Cancel a booking using customer, room and time."""

    print("\n--- CANCEL BOOKING ---")

    if not system.bookings:
        print("No bookings found.")
        return

    customer_name = input(
        "Customer name: "
    )

    try:
        room_id = int(
            input("Room ID: ")
        )

        time_slot = choose_time_slot(system)

        if time_slot is None:
            return

        booking = system.cancel_booking(
            customer_name,
            room_id,
            time_slot,
        )

        print(
            "\nBooking cancelled successfully!"
        )

        print(
            f"Customer: {booking.customer.name}"
        )
        print(
            f"Room: {booking.room.name}"
        )
        print(
            f"Time: {booking.time_slot}"
        )
        print(
            f"Status: {booking.status.value}"
        )

    except ValueError as error:
        print(f"\nError: {error}")


def show_statistics(
    system: BookingSystem,
) -> None:
    """Display booking statistics."""

    print("\n--- BOOKING STATISTICS ---")

    statistics = system.booking_statistics()

    print(
        f"Total bookings: "
        f"{statistics['total']}"
    )

    print(
        f"Confirmed bookings: "
        f"{statistics['confirmed']}"
    )

    print(
        f"Cancelled bookings: "
        f"{statistics['cancelled']}"
    )

    print(
        f"Confirmed revenue: "
        f"€{statistics['revenue']:.2f}"
    )


def show_room_summary(
    system: BookingSystem,
) -> None:
    """Display a summary of every room."""

    print("\n--- ROOM SUMMARY ---")

    summaries = system.room_summary()

    for summary in summaries:

        room = summary["room"]
        bookings = summary["bookings"]

        print("\n" + "=" * 60)
        print(room)
        print("=" * 60)

        if not bookings:
            print("No bookings.")
            continue

        print(
            f"Total bookings: {len(bookings)}"
        )

        for booking in bookings:

            print(
                f"{booking.time_slot} | "
                f"{booking.customer.name} | "
                f"{booking.status.value}"
            )


def show_menu() -> None:
    """Display the main menu."""

    print("\n")
    print("=" * 50)
    print("       MEETING ROOM BOOKING SYSTEM")
    print("=" * 50)

    print("1. Check room availability")
    print("2. Create booking")
    print("3. Show all bookings")
    print("4. Cancel booking")
    print("5. Booking statistics")
    print("6. Room summary")
    print("0. Exit")


def main() -> None:
    """Run the meeting room booking system."""

    system = BookingSystem()

    while True:

        show_menu()

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":
            show_room_availability(system)

        elif choice == "2":
            create_booking(system)

        elif choice == "3":
            show_all_bookings(system)

        elif choice == "4":
            cancel_booking(system)

        elif choice == "5":
            show_statistics(system)

        elif choice == "6":
            show_room_summary(system)

        elif choice == "0":
            print(
                "\nThank you for using "
                "the Meeting Room Booking System!"
            )
            break

        else:
            print(
                "\nInvalid choice. "
                "Please select a valid option."
            )


if __name__ == "__main__":
    main()