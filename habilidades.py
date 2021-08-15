from flask_restful import Resource

lista_habilidades = ['Python', 'Java', 'JavaScript', 'Flask']

class habilidades(Resource):
    def get(self):
        return lista_habilidades
