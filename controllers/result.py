from distutils.command.config import config
from http.client import CONFLICT
from urllib import response

from dotenv import dotenv_values
config = dotenv_values('.env')
import requests

class result():
    def __init__(self) -> None:
        pass
    
    def get_all(self, data):
        #exp_time= int(config['JWT_EXPIRATION'])
        headers = {
            "Content-Type": "application/json"
        }
        response= requests.get(url=(f"{config['URL_RESULTS']}/result/list"),json=data,headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json(),400

    def get_by_id(self, id):
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.get(url=f"{config['URL_RESULTS']}/result/{id}", headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json(),400

    def get_by_table_id(self, table):
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.get(url=f"{config['URL_RESULTS']}/political_party/table/{table}", headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json(),400 

    def get_by_candidate(self, candidate):
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.get(url=f"{config['URL_RESULTS']}/political_party/candidate/{candidate}", headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json(),400