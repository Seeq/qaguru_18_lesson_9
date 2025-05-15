import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    birth_year: str
    birth_month: str
    birth_day: str
    subjects: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str


user = User(first_name='Sergey', last_name='Labov', email='qaguru@nosuchdomain.net',
            gender='Male', phone_number='9111002030', birth_year='1989', birth_month='August', birth_day='17',
            subjects='English', hobbies='Sports, Reading, Music', picture='meme.png',
            address='First street, Second house, Third app.', state='Rajasthan',
            city='Jaiselmer')
