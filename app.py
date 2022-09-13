from msilib.schema import tables
from unittest import result
from flask import Flask, jsonify
from dotenv import dotenv_values
from flask_cors import CORS
from routes.auth_routes import auth_module

app = Flask(__name__)
cors = CORS(app)
config = dotenv_values('.env')

app.register_blueprint(auth_module,url_prefix='/auth')
app.register_blueprint(political_party , url_prefix='/political_party/list')
app.register_blueprint(table , url_prefix='/table/list')
app.register_blueprint(reports , url_prefix='/reports/list')
app.register_blueprint(result , url_prefix='/result/list')
app.config["JWT_SECRET_KEY"]=config['JWT_SECRET']

@app.route('/')
def hello_world():
    dicToReturn = {'message':'Hola Mundo'}
    return jsonify(dicToReturn)

if __name__ == '__main__':
    app.run(host='localhost', port=config["PORT"], debug=True)