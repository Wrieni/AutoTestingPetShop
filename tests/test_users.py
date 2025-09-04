
import allure
import pytest
from config.base_test import BaseTest

@allure.epic("Adminictration")
@allure.feature("Users")
class TestUsers(BaseTest):

    @pytest.mark.regression
    @allure.title("Create new user")
    def test_create_user(self):
        self.api_users.create_user()
        #print(self.api_users.get_user_by_name(user.username))