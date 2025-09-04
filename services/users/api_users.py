import requests
from config.headers import Headers
from services.users.endpoints import Endpoints
from services.users.models.usermodel import UserModel
from services.users.payloads import Payloads
from util.helper import Helper


class UserAPI(Helper):
    def __init__(self):
        super().__init__
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    def create_user(self):
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=self.payloads.create_user
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        # model = UserModel(**response.json())

        # return model
    
    def get_user_by_name(self, name):
        response = requests.get(
            url=self.endpoints.get_user_by_name(name),
            headers=self.headers.basic
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        # model = UserModel(**response.json())

        # return model
