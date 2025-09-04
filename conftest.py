from dotenv import load_dotenv
import requests
import pytest
import os

load_dotenv()

HOST = "https://petstore.swagger.io/v2" if  os.environ["STAGE"] == "qa" else "https://fakerestapi.azurewebsites.net/index.html"


@pytest.fixture(autouse=True, scope="session")
def init_enviroment():
    response = requests.get(
        url=f"{HOST}/pet/findByStatus",
        headers={"api_key": os.getenv('PETSHOP_KEY')}
    )
    assert response.status_code == 200