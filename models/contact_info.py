from dataclasses import dataclass


@dataclass
class ContactInfo:
    name: str
    email: str
    subject: str
    message: str