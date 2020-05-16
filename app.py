from flask import Flask, jsonify, request
import json

app = Flask(__name__)

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

# Lista , Altera e Exclui apenas 1 desenvolvedore
@app.route('/dev/<int:id>/', methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor ID [{}] não existe'.format(id)
            response = {'status':'erro','mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Entre em contato com o desenvolvedor.'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso','mensagem':'Registro excluido.'})

# Lista todos os desenvolvedroes e insere novos
@app.route('/dev/', methods=['GET','POST'])
def lista_desenvolvedore():
    if request.method == 'POST':
        dados = json.loads(request.data)
        pos = len(desenvolvedores)
        dados['id'] = pos
        desenvolvedores.append(dados)
        #return jsonify({'status':'sucesso','mensagem':'Registro inserido.'})
        return jsonify(desenvolvedores[pos])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)