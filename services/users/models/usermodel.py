from pydantic import BaseModel, field_validator

class UserModel(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int

    @field_validator("email", "firstName", "lastName", "username")
    def fields_are_not_empry(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value