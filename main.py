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


