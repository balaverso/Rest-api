from flask_restful import Resource, reqparse
from models.moeda import MoedaModel

class Moedas(Resource):
    def get(self):
        return {'moedas': [moeda.json() for moeda in MoedaModel.query.all()]} # SELECT * FROM hoteis

class Moeda(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome', type=str, required=True, help="O campo 'nome' não pode ser deixado em branco.")
    atributos.add_argument('fechou')
    atributos.add_argument('volume')
    atributos.add_argument('categoria')

    def get(self, moeda_id):
        moeda = MoedaModel.find_moeda(moeda_id)
        if moeda:
            return moeda.json()
        return {'message': 'Moeda não encontrada.'}, 404

    def post(self, moeda_id):
        if MoedaModel.find_moeda(moeda_id):
            return {"message": "Moeda id '{}' já existe.".format(moeda_id)}, 400 #Bad Request

        dados = Moeda.atributos.parse_args()
        moeda = MoedaModel(moeda_id, **dados)
        try:
            moeda.save_moeda()
        except:
            return {"message": "Um erro ocorreu ao tentar criar a moeda."}, 500 #Internal Server Error
        return moeda.json(), 201

    def put(self, moeda_id):
        dados = Moeda.atributos.parse_args()
        moeda = MoedaModel(moeda_id, **dados)

        moeda_encontrada = MoedaModel.find_moeda(moeda_id)
        if moeda_encontrada:
            moeda_encontrada.update_moeda(**dados)
            moeda_encontrada.save_moeda()
            return moeda_encontrada.json(), 200
        moeda.save_moeda()
        return moeda.json(), 201

    def delete(self, moeda_id):
        moeda = MoedaModel.find_moeda(moeda_id)
        if moeda:
            moeda.delete_moeda()
            return {'message': 'Moeda deletada.'}
        return {'message': 'Moeda Não encontrada.'}, 404
