from distutils.command.config import config
from http.client import CONFLICT
from urllib import response

from dotenv import dotenv_values
config = dotenv_values('.env')
import requests

class political_party():
    def __init__(self) -> None:
        pass
    
    def get_all(self, data):
        #exp_time= int(config['JWT_EXPIRATION'])
        headers = {
            "Content-Type": "application/json"
        }
        response= requests.get(url=(f"{config['URL_RESULTS']}/political_party/list"),json=data,headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json() 

    def get_by_id(self, id):
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.get(url=f"{config['URL_RESULTS']}/political_party/{id}", headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json() 

    def get_by_lema_id(self, lema):
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.get(url=f"{config['URL_RESULTS']}/political_party/lema/{lema}", headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json() 

    def get_by_nombre(self, nombre):
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.get(url=f"{config['URL_RESULTS']}/political_party/nombre/{nombre}", headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json() 

    def create(self,data,political_party):
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url=f"{config['URL_RESULTS']}/political_party/{political_party}",json=data, headers=headers)
        print(response.status_code)
        if response.status_code == 201:
            return response.json(), 200
        return response.json(), 400

    def update(self,id,data):
        # headers = {
        #     "Content-Type": "application/json"
        # }
        # response = requests.put(url=f"{config['URL_RESULTS']}/candidate/{id}",json=data, headers=headers)
        # print(response.status_code)
        # if response.status_code == 201:
        #     return response.json(), 200
        # return response.json(), 400
        pass

    def delete(self,data):
        pass