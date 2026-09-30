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


