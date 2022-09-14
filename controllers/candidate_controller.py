from distutils.command.config import config
from http.client import CONFLICT
from urllib import response


from dotenv import dotenv_values
config = dotenv_values('.env')
import requests

class CandidateController():
    def __init__(self) -> None:
        pass
    
    def get_all(self, data):
        #exp_time= int(config['JWT_EXPIRATION'])
        headers = {
            "Content-Type": "application/json"
        }
        response= requests.get(url=(f"{config['URL_RESULTS']}/candidate/list"),json=data,headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json() 

    def get_by_id(self, id):
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.get(url=f"{config['URL_RESULTS']}/candidate/{id}", headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json() 

    def get_by_document_id(self, document):
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.get(url=f"{config['URL_RESULTS']}/candidate/document/{document}", headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json() 

    def get_by_resolution(self, resolution):
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.get(url=f"{config['URL_RESULTS']}/candidate/resolution/{resolution}", headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json() 

    def create(self,data,political_party):
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url=f"{config['URL_RESULTS']}/candidate/{political_party}",json=data, headers=headers)
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