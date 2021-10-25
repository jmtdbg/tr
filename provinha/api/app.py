from flask import Flask
from flask_restful import Api
from resources.residencia import Residencias, Residencia
from flask_cors import CORS


app = Flask(__name__)
# caminho e configuração do banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
CORS(app)


# cria banco
@app.before_first_request
def cria_banco():
    banco.create_all()

# adicionando os recursos
api.add_resource(Residencias, '/residencias')
api.add_resource(Residencia, '/residencias/<int:id>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
