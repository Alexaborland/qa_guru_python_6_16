import dataclasses
import datetime


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    sex: str
    mobile_number: str
    date_of_birth: datetime.date
    subject: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str


Alexandra = User(
    first_name='Alexandra',
    last_name='Borland',
    email='borland3711@gmail.com',
    sex='Female',
    mobile_number='9992131512',
    date_of_birth=datetime.date(day=15, month=6, year=1998),
    subject='Maths',
    hobbies='Music',
    picture='img.png',
    address='Kondratyevsky prospect',
    state='Haryana',
    city='Karnal',
)
