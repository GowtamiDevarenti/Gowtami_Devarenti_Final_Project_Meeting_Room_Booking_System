from enum import Enum


class BookingStatus(Enum):
    """Possible statuses for a booking."""

    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"


class Customer:
    """Represents a customer who makes a booking."""

    def __init__(
        self,
        customer_id: int,
        name: str,
        email: str,
    ) -> None:

        if not name.strip():
            raise ValueError("Customer name cannot be empty.")

        if "@" not in email:
            raise ValueError("Please enter a valid email address.")

        self.customer_id = customer_id
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f"{self.customer_id}: {self.name} ({self.email})"
    


class MeetingRoom:
    """Represents a standard meeting room."""

    def __init__(
        self,
        room_id: int,
        name: str,
        capacity: int,
        hourly_rate: float,
    ) -> None:

        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")

        if hourly_rate < 0:
            raise ValueError("Hourly rate cannot be negative.")

        self.room_id = room_id
        self.name = name
        self.capacity = capacity
        self.hourly_rate = hourly_rate

    def calculate_cost(self) -> float:
        """Return the cost for one hour."""

        return self.hourly_rate

    def room_type(self) -> str:
        return "Meeting Room"

    def __str__(self) -> str:
        return (
            f"{self.room_id}: {self.name} | "
            f"{self.room_type()} | "
            f"Capacity: {self.capacity} | "
            f"€{self.hourly_rate:.2f}/hour"
        )


class ConferenceRoom(MeetingRoom):
    """Represents a conference room."""

    EQUIPMENT_FEE = 25.0

    def __init__(
        self,
        room_id: int,
        name: str,
        capacity: int,
        hourly_rate: float,
        has_projector: bool = True,
    ) -> None:

        super().__init__(
            room_id,
            name,
            capacity,
            hourly_rate,
        )

        self.has_projector = has_projector

    def calculate_cost(self) -> float:
        """Return hourly room cost plus equipment fee."""

        return self.hourly_rate + self.EQUIPMENT_FEE

    def room_type(self) -> str:
        return "Conference Room"

    def __str__(self) -> str:
        projector = "Yes" if self.has_projector else "No"

        return (
            f"{self.room_id}: {self.name} | "
            f"{self.room_type()} | "
            f"Capacity: {self.capacity} | "
            f"€{self.hourly_rate:.2f}/hour | "
            f"Projector: {projector}"
        )


class Booking:
    """Represents one room booking."""

    def __init__(
        self,
        booking_id: int,
        customer: Customer,
        room: MeetingRoom,
        time_slot: str,
    ) -> None:

        self.booking_id = booking_id
        self.customer = customer
        self.room = room
        self.time_slot = time_slot
        self.status = BookingStatus.CONFIRMED
        self.cost = room.calculate_cost()

    def cancel(self) -> None:
        """Cancel the booking."""

        if self.status == BookingStatus.CANCELLED:
            raise ValueError("Booking is already cancelled.")

        self.status = BookingStatus.CANCELLED

    def conflicts_with(self, time_slot: str) -> bool:
        """Check whether this booking uses the given time slot."""

        if self.status == BookingStatus.CANCELLED:
            return False

        return self.time_slot == time_slot

    def __str__(self) -> str:
        return (
            f"Booking #{self.booking_id} | "
            f"Customer: {self.customer.name} | "
            f"Room: {self.room.name} | "
            f"Room ID: {self.room.room_id} | "
            f"Time: {self.time_slot} | "
            f"Status: {self.status.value} | "
            f"Cost: €{self.cost:.2f}"
        )
        

class MeetingRoom:
    """Represents a standard meeting room."""

    def __init__(
        self,
        room_id: int,
        name: str,
        capacity: int,
        hourly_rate: float,
    ) -> None:

        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")

        if hourly_rate < 0:
            raise ValueError("Hourly rate cannot be negative.")

        self.room_id = room_id
        self.name = name
        self.capacity = capacity
        self.hourly_rate = hourly_rate

    def calculate_cost(self) -> float:
        """Return the cost for one hour."""

        return self.hourly_rate

    def room_type(self) -> str:
        return "Meeting Room"

    def __str__(self) -> str:
        return (
            f"{self.room_id}: {self.name} | "
            f"{self.room_type()} | "
            f"Capacity: {self.capacity} | "
            f"€{self.hourly_rate:.2f}/hour"
        )


class ConferenceRoom(MeetingRoom):
    """Represents a conference room."""

    EQUIPMENT_FEE = 25.0

    def __init__(
        self,
        room_id: int,
        name: str,
        capacity: int,
        hourly_rate: float,
        has_projector: bool = True,
    ) -> None:

        super().__init__(
            room_id,
            name,
            capacity,
            hourly_rate,
        )

        self.has_projector = has_projector

    def calculate_cost(self) -> float:
        """Return hourly room cost plus equipment fee."""

        return self.hourly_rate + self.EQUIPMENT_FEE

    def room_type(self) -> str:
        return "Conference Room"

    def __str__(self) -> str:
        projector = "Yes" if self.has_projector else "No"

        return (
            f"{self.room_id}: {self.name} | "
            f"{self.room_type()} | "
            f"Capacity: {self.capacity} | "
            f"€{self.hourly_rate:.2f}/hour | "
            f"Projector: {projector}"
        )


class Booking:
    """Represents one room booking."""

    def __init__(
        self,
        booking_id: int,
        customer: Customer,
        room: MeetingRoom,
        time_slot: str,
    ) -> None:

        self.booking_id = booking_id
        self.customer = customer
        self.room = room
        self.time_slot = time_slot
        self.status = BookingStatus.CONFIRMED
        self.cost = room.calculate_cost()

    def cancel(self) -> None:
        """Cancel the booking."""

        if self.status == BookingStatus.CANCELLED:
            raise ValueError("Booking is already cancelled.")

        self.status = BookingStatus.CANCELLED

    def conflicts_with(self, time_slot: str) -> bool:
        """Check whether this booking uses the given time slot."""

        if self.status == BookingStatus.CANCELLED:
            return False

        return self.time_slot == time_slot

    def __str__(self) -> str:
        return (
            f"Booking #{self.booking_id} | "
            f"Customer: {self.customer.name} | "
            f"Room: {self.room.name} | "
            f"Room ID: {self.room.room_id} | "
            f"Time: {self.time_slot} | "
            f"Status: {self.status.value} | "
            f"Cost: €{self.cost:.2f}"
        )