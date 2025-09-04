from faker import Faker

fake = Faker()
class Payloads:

    create_user = {
        "username": fake.user_name(),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(length=10),
        "phone": fake.phone_number(),
        # "userStatus": 0
    }

