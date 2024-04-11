from faker import Faker

from data.data import User

fake = Faker()


def generated_user():
    password = fake.password()
    yield User(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        password=password,
        confirm_password=password,
    )
