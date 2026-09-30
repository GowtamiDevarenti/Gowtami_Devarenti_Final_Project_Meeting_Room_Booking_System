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
    