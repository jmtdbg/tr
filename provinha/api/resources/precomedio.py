from flask_restful import Resource, reqparse
from models.precomedio import PrecoMedioModel
from resources.filtros import normalize_path_params_pm, consulta_com_ng_mp, consulta_sem_ng_mp
import sqlite3


path_params = reqparse.RequestParser()
path_params.add_argument('neighbourhood_group', type=str)
path_params.add_argument('room_type', type=str)
path_params.add_argument('price', type=float)
path_params.add_argument('limit', type=float)
path_params.add_argument('offset', type=float)

class PrecoMedio(Resource):
    def get(self):
        connection = sqlite3.connect('banco.db')
        cursor = connection.cursor()

        dados = path_params.parse_args()
        dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None}
        parametros = normalize_path_params_pm(**dados_validos)

        if not parametros.get('neighbourhood_group'):
            tupla = tuple([parametros[chave] for chave in parametros])
            resultado = cursor.execute(consulta_sem_ng_mp, tupla)
        else:
            tupla = tuple([parametros[chave] for chave in parametros])
            resultado = cursor.execute(consulta_com_ng_mp, tupla)

        precomedios = []
        for linha in resultado:
            precomedios.append({
            'neighbourhood_group': linha[0] ,
            'room_type': linha[1],
            'price': linha[2],
            })

        return {'precomedios': precomedios} # SELECT * FROM precomedios

class PrecoMedioAll(Resource):
    
    def get(self):
        #SELECT * FROM residencias
        return {'precomedios': [precomedio.json() for precomedio in PrecoMedioModel.query.all()]} 