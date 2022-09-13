from dotenv import dotenv_values
import requests
config = dotenv_values('.env')

class political_party():
  def __init__(self):
    pass
  
  def create(self, data):
    headers = {
      "Content-Type": "application/json"
    }
    response = requests.post(url=f"{config['URL_ACADEMIC']}/political_party/list",json=data, headers=headers)
    print(response.status_code)
    if response.status_code == 201:
      return response.json(), 200
    return response.json(), 400