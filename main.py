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


