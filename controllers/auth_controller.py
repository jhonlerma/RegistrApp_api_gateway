from distutils.command.config import config
from http.client import CONFLICT
from urllib import response


from dotenv import dotenv_values
config = dotenv_values('.env')
import requests

class AuthContoller():
    def __init__(self) -> None:
        pass

    def login(self, data):
        exp_time= int(config['JWT_EXPIRATION'])
        headers = {
            "Content-Type": "application/json"
        }
        response= requests.post(url=(f"{config['URL_AUTH']}/auth/"),json=data,headers=headers)
        print(response.json())
        return response.json()