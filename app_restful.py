from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id':0,
    'nome':'Edson',
    'habilidades':['Python','Flask']},
    {'id':1,
    'nome':'Joao',
    'habilidades':['Java','Tomcat']},
    {'id':2,
    'nome':'Elias',
    'habilidades':['Python','Django']},
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor ID [{}] não existe'.format(id)
            response = {'status':'erro','mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Entre em contato com o desenvolvedor.'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        response = {'status': 'sucesso', 'mensagem': 'Registro excluido.'}
        return response

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

class IncluiDesenvolvedores(Resource):
    def post(self):
        dados = json.loads(request.data)
        pos = len(desenvolvedores)
        dados['id'] = pos
        desenvolvedores.append(dados)
        return desenvolvedores[pos]

api.add_resource(Desenvolvedor,'/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores,'/dev/listar/')
api.add_resource(IncluiDesenvolvedores,'/dev/incluir/')
api.add_resource(Habilidades,'/dev/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)