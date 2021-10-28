from flask import Flask
from flask_restful import Api
from resources.residencia import Residencias, Residencia, ResidenciaLike, ResidenciasFiltro
from resources.precomedio import PrecoMedio, PrecoMedioAll
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
api.add_resource(Residencias, '/residencias/all/page/<int:page>/', methods=['GET'])
api.add_resource(Residencia, '/residencias/<int:id>')
api.add_resource(PrecoMedioAll, '/preco-medio/all')

#1. Lista de todas as residências com opção de filtros via query string
api.add_resource(ResidenciasFiltro, '/residencias')

# 2. Média de preços por 'neighbourhood_group' e 'room_type'
api.add_resource(PrecoMedio, '/preco-medio')

# 3. Salvar um "like" da propriedade
api.add_resource(ResidenciaLike, '/residencias/like/<int:id>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
