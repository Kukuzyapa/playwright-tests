from dataclasses import dataclass
@dataclass
class Address:
    first_name: str
    last_name: str
    company: str
    address: str
    address2: str
    country: str
    state: str
    city: str
    zipcode: str
    mobile_number: str

@dataclass
class DateOfBirth:
    day: str
    month: str
    year: str

@dataclass
class RegisterUser:
    title: str
    name: str
    email: str
    password: str
    date_of_birth: DateOfBirth
    newsletter: bool
    special_offers: bool
    address: Address

    def __post_init__(self):
        self.date_of_birth = DateOfBirth(**self.date_of_birth)
        self.address = Address(**self.address)