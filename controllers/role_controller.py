from flask import jsonify
from dotenv import dotenv_values
config = dotenv_values('.env')
import requests


class RoleController():
    
    def __init__(self) -> None:
       pass
     
    def get_all(self, data):
        exp_time= int(config['JWT_EXPIRATION'])
        headers = {
            "Content-Type": "application/json"
        }
        response= requests.get(url=(f"{config['URL_AUTH']}/roles/"),json=data,headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json(),

    def get_by_rol(self, role):
        exp_time= int(config['JWT_EXPIRATION'])
        headers = {
      "Content-Type": "application/json"
    }
        response = requests.get(url=f"{config['URL_AUTH']}/roles/{role}", headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json(),