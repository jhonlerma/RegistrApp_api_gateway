from flask import jsonify
from dotenv import dotenv_values
config = dotenv_values('.env')
import requests


class UsersController():
    
    def __init__(self) -> None:
       pass
     
    def get_all(self, data):
        exp_time= int(config['JWT_EXPIRATION'])
        headers = {
            "Content-Type": "application/json"
        }
        response= requests.get(url=(f"{config['URL_AUTH']}/users/"),json=data,headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json(),

    def get_by_id(self, id):
        exp_time= int(config['JWT_EXPIRATION'])
        headers = {
      "Content-Type": "application/json"
    }
        response = requests.get(url=f"{config['URL_AUTH']}/users/{id}", headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json(),

    
    def create(self, data):
        exp_time= int(config['JWT_EXPIRATION'])
        headers = {
            "Content-Type": "application/json"
        }
        response= requests.post(url=(f"{config['URL_AUTH']}/users/"),json=data,headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json(),

    def delete_by_id(self, id):
        exp_time= int(config['JWT_EXPIRATION'])
        headers = {
      "Content-Type": "application/json"
    }
        response = requests.delete(url=f"{config['URL_AUTH']}/users/{id}", headers=headers)
        if response.status_code == 204:
            return {}, 204
        return {"error":"no permitido"},400

    def update(self, id, data):
        exp_time= int(config['JWT_EXPIRATION'])
        headers = {
      "Content-Type": "application/json"
    }
        response = requests.put(url=f"{config['URL_AUTH']}/users/{id}",json=data,headers=headers)
        if response.status_code == 204:
            return {}, 204
        return {},400
        
    def get_by_rol(self, role):
        exp_time= int(config['JWT_EXPIRATION'])
        headers = {
      "Content-Type": "application/json"
    }
        response = requests.get(url=f"{config['URL_AUTH']}/users/roles/{role}", headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json(),


