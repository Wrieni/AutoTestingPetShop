import os

HOST = "https://petstore.swagger.io/v2" if  os.environ["STAGE"] == "qa" else "https://fakerestapi.azurewebsites.net/index.html"

class Endpoints:

    create_user = f"{HOST}/user"
    get_user_by_name = lambda self, username: f"{HOST}/user/{username}"

    # get_user_by_name("")