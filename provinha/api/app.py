from flask import Flask
from flask_restful import Api
from resources.residencia import Residencias, Residencia


app = Flask(__name__)
api = Api(app)


# adicionando os recursos
api.add_resource(Residencias, '/residencias')
api.add_resource(Residencia, '/residencias/<int:residencia_id>')

if __name__ == '__main__':
    app.run(debug=True)
