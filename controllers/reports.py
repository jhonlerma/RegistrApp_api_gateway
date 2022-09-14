from dotenv import dotenv_values
import requests
config = dotenv_values('.env')

class reports():
  def __init__(self):
    pass
  
  def get_all(self, data):
    headers = {
      "Content-Type": "application/json"
    }
    response = requests.get(url=f"{config['URL_RESULTS']}/report/list",json=data, headers=headers)
    print(response.status_code)
    if response.status_code == 201:
      return response.json(), 200
    return response.json(), 400