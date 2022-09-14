from msilib.schema import tables
from routes.political_party import political_party_module
from routes.table import table_module
from routes.reports import reports_module
from routes.result import  result_module
from flask import Flask, jsonify
from dotenv import dotenv_values
from flask_cors import CORS
from routes.auth_routes import auth_module

app = Flask(__name__)
cors = CORS(app)
config = dotenv_values('.env')

app.register_blueprint(auth_module,url_prefix='/auth')
app.register_blueprint(political_party_module , url_prefix='/political_party')
app.register_blueprint(table_module , url_prefix='/table')
app.register_blueprint(reports_module , url_prefix='/report')
app.register_blueprint(result_module , url_prefix='/result')
app.config["JWT_SECRET_KEY"]=config['JWT_SECRET']

@app.route('/')
def hello_world():
    dicToReturn = {'message':'Hola Mundo'}
    return jsonify(dicToReturn)

if __name__ == '__main__':
    app.run(host='localhost', port=config["PORT"], debug=True)