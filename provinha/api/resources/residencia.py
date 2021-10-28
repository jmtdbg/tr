from flask_restful import Resource, reqparse
from sqlalchemy.orm import query_expression
from models.residencia import ResidenciaModel, ResidenciaLikeModel
from resources.filtros import normalize_path_params, consulta_com_ng, consulta_sem_ng
# from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, current_app, request, jsonify, url_for
import sqlite3

# Recebendo parametros opcionais
path_params = reqparse.RequestParser()
path_params.add_argument('id', type=int)
path_params.add_argument('name', type=str)
path_params.add_argument('host_id', type=str)
path_params.add_argument('host_name', type=str)
path_params.add_argument('neighbourhood_group', type=str)
path_params.add_argument('neighbourhood', type=str)
path_params.add_argument('latitude', type=str)
path_params.add_argument('longitude', type=str)
path_params.add_argument('room_type', type=str)
path_params.add_argument('price', type=str)
path_params.add_argument('minimum_nights', type=str)
path_params.add_argument('number_of_reviews', type=str)
path_params.add_argument('last_review', type=str)
path_params.add_argument('reviews_per_month', type=str)
path_params.add_argument('calculated_host_listings_count', type=str)
path_params.add_argument('availability_365', type=str)
path_params.add_argument('like', type=str)
path_params.add_argument('limit', type=float)
path_params.add_argument('offset', type=float)

class ResidenciasFiltro(Resource):
    def get(self):
    
        # conecção com o sqlite
        connection = sqlite3.connect('banco.db')
        cursor = connection.cursor()

        # Recebe os parâmetros opcionais
        dados = path_params.parse_args()
        # valida se estão vazios
        dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None}
        # dicionário com os parametros
        parametros = normalize_path_params(**dados_validos)
        # consultas 
        if not parametros.get('neighbourhood_group'):
            tupla = tuple([parametros[chave] for chave in parametros])
            resultado = cursor.execute(consulta_sem_ng, tupla)
        else:
            tupla = tuple([parametros[chave] for chave in parametros])
            resultado = cursor.execute(consulta_com_ng, tupla)
        # 
        residencias = []
        for linha in resultado:
            residencias.append({
                'id': linha[0],  
                'name': linha[1],
                'host_id': linha[2],
                'host_name': linha[3],
                'neighbourhood_group': linha[4],
                'neighbourhood': linha[5],
                'latitude': linha[6],
                'longitude': linha[7],
                'room_type': linha[8],
                'price': linha[9],
                'minimum_nights': linha[10],
                'number_of_reviews': linha[11],
                'last_review': linha[12],
                'reviews_per_month': linha[13],
                'calculated_host_listings_count': linha[14],
                'availability_365': linha[15],
                'like': linha[16]
            })
        return {'residencias': residencias} # SELECT * FROM residencias

# Todas as residencias
class Residencias(Resource):
    def get(self, page=1):
        # return {'residencias': [residencia.json() for residencia in ResidenciaModel.query.all()]} 
        
        return {'residencias': [residencia.json() for residencia in ResidenciaModel.query.limit(10).offset(0)]}  
        
        # return {'residencias': [residencia.json() for residencia in ResidenciaModel.query.paginate(per_page=2, page=page, error_out=False)]} 
        
        # result = ResidenciaModel.query.paginate(per_page=2, page=page, error_out=False)
        # return result.json
          


    # def get(self, page=1):
    #     result = ResidenciaModel.query.paginate(page, 10)
    #     return jsonify({
    #         'page': page,
    #         'residencias': result,
    #         'total pages': result.pages,
    #         'total per pages': result.per_page,
    #         'next page': f'{url_for("residencias.residencias")}{result.next_num}',
    #         'previous page': f'{url_for("residencias.residencias")}{result.prev_num}',
    #     }
    #     ), 200

# Like em residencia
class ResidenciaLike(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('like')

    # POST LIKE
    def post(self, id):
        if ResidenciaLikeModel.find_residencia(id):
            return {"message" : "Residência id '{}' já tem like.".format(id)}, 400 # Pedido ruin 

        dados = ResidenciaLike.atributos.parse_args()
        residencia = ResidenciaLikeModel(id, **dados)
        try:
            residencia.save_residencia()
        except:
            return {'message': 'Erro interno ao tentar salvar a residencia.'}, 500 # Erro interno do servidor
        return residencia.json()

class Residencia(Resource):   
    # Definindo argumentos
    atributos = reqparse.RequestParser()
    # atributos.add_argument('id')

    atributos.add_argument('name', type=str, required=True, help="O campo 'name' é obrigatório.")
    atributos.add_argument('host_id')
    atributos.add_argument('host_name')
    atributos.add_argument('neighbourhood_group')
    atributos.add_argument('neighbourhood')
    atributos.add_argument('latitude')
    atributos.add_argument('longitude')
    atributos.add_argument('room_type')
    atributos.add_argument('price')
    atributos.add_argument('minimum_nights')
    atributos.add_argument('number_of_reviews')
    atributos.add_argument('last_review')
    atributos.add_argument('reviews_per_month')
    atributos.add_argument('calculated_host_listings_count')
    atributos.add_argument('availability_365')
    atributos.add_argument('like')

    
    # GET
    def get(self, id):
        residencia = ResidenciaModel.find_residencia(id)
        if residencia:
            return residencia.json()
        return {'message': 'Residência nao encontrada!!!'}, 404 #Não existe
    
    # POST
    def post(self, id):
        if ResidenciaModel.find_residencia(id):
            return {"message" : "Residência id '{}' já existe.".format(id)}, 400 # Pedido ruin 

        dados = Residencia.atributos.parse_args()
        residencia = ResidenciaModel(id, **dados)
        try:
            residencia.save_residencia()
        except:
            return {'message': 'Erro interno ao tentar salvar a residencia.'}, 500 # Erro interno do servidor
        return residencia.json()
    
    # PUT
    def put(self, id):
        dados = Residencia.atributos.parse_args()
        # pesquisa residencia
        residencia_encontrada = ResidenciaModel.find_residencia(id)
        # se não existir cria uma nova
        if residencia_encontrada:
            residencia_encontrada.update_residencia(**dados)
            residencia_encontrada.save_residencia()
            return residencia_encontrada.json(), 200 #OK
        residencia = ResidenciaModel(id, **dados)
        try:
            residencia.save_residencia()
        except:
            return {'message': 'Erro interno ao tentar salvar a residencia.'}, 500 # Erro interno do servidor        
        return residencia.json(), 201 #Criado
    
    # DELETE
    def delete(self, id):
        # pesquisa residencia
        residencia = ResidenciaModel.find_residencia(id)

        if residencia:
            try:
                residencia.delete_residencia()
            except:
                return {'message': 'Erro interno ao tentar deletar a residencia.'}, 500 # Erro interno do servidor
        
            return {'message': 'Residência deletada.'}
        return {'message': 'Residência não existe.'}, 404
