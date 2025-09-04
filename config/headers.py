import os
from dotenv import load_dotenv

load_dotenv()

class Headers:
    basic = {
        "api_key": os.getenv('PETSHOP_KEY')
    }