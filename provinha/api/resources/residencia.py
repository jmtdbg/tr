from flask_restful import Resource, reqparse
from models.residencia import ResidenciaModel

# from api.models import residencia
# import sqlite3

# residencias = [
#     {
#         'id': 36411407,
#         'name': 'Brand  new  1  bedroom  steps  from  Soho!',
#         'host_id': 33917435,
#         'host_name': 'Mike',
#         'neighbourhood_group': 'Manhattan2',
#         'neighbourhood': 'Lower  East  Side',
#         'latitude': 40.71825,
#         'longitude': -73.99019,
#         'room_type': 'Entire  home/apt',
#         'price': 150,
#         'minimum_nights': 4,
#         'number_of_reviews': 1,
#         'last_review': '2019-07-06',
#         'reviews_per_month': 1.0,
#         'calculated_host_listings_count': 1,
#         'availability_365': 13
#     },
#     {
#         'id': 36425863,
#         'name': 'Lovely  Privet  Bedroom  with  Privet  Restroom',
#         'host_id': 83554966,
#         'host_name': 'Rusaa',
#         'neighbourhood_group': 'Manhattan',
#         'neighbourhood': 'Upper  East  Side',
#         'latitude': 40.78099,
#         'longitude': -73.95366,
#         'room_type': 'Private  room',
#         'price': 129,
#         'minimum_nights': 1,
#         'number_of_reviews': 1, 
#         'last_review': '2019-07-07', 
#         'reviews_per_month': 1.0,
#         'calculated_host_listings_count': 1,  
#         'availability_365': 147	  
#     }
# ]

# Tratando parametros vazios e parametros default
# def normalize_path_params(id = None, neighbourhood_group = None, limit = 50, offset = 0):
#     if neighbourhood_group:
#         return {
#             'id': id,
#             'neighbourhood_group': neighbourhood_group,
#             'limit': limit,
#             'offset': offset}
#     return {
#             'id': id,
#             'neighbourhood_group': neighbourhood_group,
#             'limit': limit,
#             'offset': offset}


# # Recebendo parametros opcionais
# path_params = reqparse.RequestParser()
# path_params.add_argument('id', type=int)
# path_params.add_argument('neighbourhood_group', type=str)
# path_params.add_argument('limit', type=float)
# path_params.add_argument('offset', type=float)
class Residencias(Resource):
    def get(self):
        #SELECT * FROM residencias
        return {'residencias': [residencia.json() for residencia in ResidenciaModel.query.all()]} 
    
    # def get(self):
    #     # conecção com o sqlite
    #     connection = sqlite3.connect('banco.db')
    #     cursor = connection.cursor()

    #     # Recebe os parâmetros opcionais
    #     dados = path_params.parse_args()
    #     # valida se estão vazios
    #     dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None}
    #     # dicionário com os parametros
    #     parametros = normalize_path_params(**dados_validos)

    #     if not parametros.get('residencia'):
    #         consulta = "SELECT * FROM residencias \
    #         WHERE (neighbourhood_group = ?) LIMIT ? OFFSET ?"
    #         tupla = tupla([parametros[chave] for chave in parametros])
    #         resultado = cursor.execute(consulta, tupla)
    #     else:
    #         consulta = "SELECT * FROM residencias \
    #         WHERE (neighbourhood_group = ?) LIMIT ? OFFSET ?"
    #         tupla = tupla([parametros[chave] for chave in parametros])
    #         resultado = cursor.execute(consulta, tupla)

    #     residencias = []
    #     for linha in resultado:
    #         residencias.append({
    #             'id': linha[0],  
    #             'name': linha[1],
    #             'host_id': linha[2],
    #             'host_name': linha[3],
    #             'neighbourhood_group': linha[4],
    #             'neighbourhood': linha[5],
    #             'latitude': linha[6],
    #             'longitude': linha[7],
    #             'room_type': linha[8],
    #             'price': linha[9],
    #             'minimum_nights': linha[10],
    #             'number_of_reviews': linha[11],
    #             'last_review': linha[12],
    #             'reviews_per_month': linha[13],
    #             'calculated_host_listings_count': linha[14],
    #             'availability_365': linha[15]
    #         })

    #     return {'residencias' : residencias}
    #     # return {'residencias' : [residencia.json() for residencia in ResidenciaModel.query()]}

class Residencia(Resource):   
    # Definindo argumentos
    atributos = reqparse.RequestParser()
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
