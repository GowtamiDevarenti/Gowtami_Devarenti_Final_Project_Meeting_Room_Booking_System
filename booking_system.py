from models import (
    Booking,
    BookingStatus,
    ConferenceRoom,
    Customer,
    MeetingRoom,
)


class BookingSystem:
    """Manages customers, rooms and bookings."""

    TIME_SLOTS = [
        "09:00 - 10:00",
        "10:00 - 11:00",
        "11:00 - 12:00",
    ]

    def __init__(self) -> None:

        self.customers: dict[int, Customer] = {}
        self.rooms: dict[int, MeetingRoom] = {}
        self.bookings: dict[int, Booking] = {}

        self._next_customer_id = 1
        self._next_booking_id = 1

        self._create_default_rooms()

    def _create_default_rooms(self) -> None:
        """Create the four fixed rooms."""

        self.rooms[101] = MeetingRoom(
            room_id=101,
            name="Meeting Room A",
            capacity=6,
            hourly_rate=40.0,
        )

        self.rooms[102] = MeetingRoom(
            room_id=102,
            name="Meeting Room B",
            capacity=8,
            hourly_rate=50.0,
        )

        self.rooms[201] = ConferenceRoom(
            room_id=201,
            name="Conference Room A",
            capacity=12,
            hourly_rate=70.0,
            has_projector=True,
        )

        self.rooms[202] = ConferenceRoom(
            room_id=202,
            name="Conference Room B",
            capacity=20,
            hourly_rate=90.0,
            has_projector=True,
        )

    def get_room(self, room_id: int) -> MeetingRoom:
        """Find a room using its ID."""

        if room_id not in self.rooms:
            raise ValueError("Room not found.")

        return self.rooms[room_id]

    def get_available_rooms(
        self,
        time_slot: str,
    ) -> list[MeetingRoom]:
        """Return rooms available for a selected time slot."""

        if time_slot not in self.TIME_SLOTS:
            raise ValueError("Invalid time slot.")

        available_rooms = []

        for room in self.rooms.values():

            if self.is_room_available(
                room,
                time_slot,
            ):
                available_rooms.append(room)

        return available_rooms

    def is_room_available(
        self,
        room: MeetingRoom,
        time_slot: str,
    ) -> bool:
        """Check whether a room is available."""

        if time_slot not in self.TIME_SLOTS:
            return False

        for booking in self.bookings.values():

            if booking.room.room_id != room.room_id:
                continue

            if booking.conflicts_with(time_slot):
                return False

        return True

    def create_booking(
        self,
        name: str,
        email: str,
        room_id: int,
        time_slot: str,
    ) -> Booking:
        """Create a customer and booking."""

        if time_slot not in self.TIME_SLOTS:
            raise ValueError("Invalid time slot.")

        room = self.get_room(room_id)

        if not self.is_room_available(
            room,
            time_slot,
        ):
            raise ValueError(
                "This room is already booked for this time slot."
            )

        customer = Customer(
            self._next_customer_id,
            name,
            email,
        )

        self.customers[customer.customer_id] = customer
        self._next_customer_id += 1

        booking = Booking(
            self._next_booking_id,
            customer,
            room,
            time_slot,
        )

        self.bookings[booking.booking_id] = booking
        self._next_booking_id += 1

        return booking

    def cancel_booking(
        self,
        customer_name: str,
        room_id: int,
        time_slot: str,
    ) -> Booking:
        """Cancel a booking using customer, room and time."""

        for booking in self.bookings.values():

            if (
                booking.customer.name.lower()
                == customer_name.lower()
                and booking.room.room_id == room_id
                and booking.time_slot == time_slot
            ):

                booking.cancel()
                return booking

        raise ValueError(
            "No matching booking found."
        )

    def booking_statistics(self) -> dict[str, float]:
        """Return booking statistics."""

        total = len(self.bookings)

        confirmed = len(
            [
                booking
                for booking in self.bookings.values()
                if booking.status == BookingStatus.CONFIRMED
            ]
        )

        cancelled = len(
            [
                booking
                for booking in self.bookings.values()
                if booking.status == BookingStatus.CANCELLED
            ]
        )

        revenue = sum(
            booking.cost
            for booking in self.bookings.values()
            if booking.status == BookingStatus.CONFIRMED
        )

        return {
            "total": total,
            "confirmed": confirmed,
            "cancelled": cancelled,
            "revenue": revenue,
        }

    def room_summary(self) -> list[dict[str, object]]:
        """Return booking information for every room."""

        summaries = []

        for room in self.rooms.values():

            room_bookings = [
                booking
                for booking in self.bookings.values()
                if booking.room.room_id == room.room_id
            ]

            summaries.append(
                {
                    "room": room,
                    "bookings": room_bookings,
                }
            )

        return summaries