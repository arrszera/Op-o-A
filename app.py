from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista em memória para armazenar as mensagens
mensagens = []

@app.route('/webhook', methods=['POST'])
def receber_webhook():
    dados = request.get_json()
    if dados:
        mensagens.append(dados)
        return jsonify({"status": "sucesso", "mensagem": "Dados registrados"}), 201
    return jsonify({"erro": "Nenhum dado JSON recebido"}), 400

@app.route('/mensagens', methods=['GET'])
def listar_mensagens():
    return jsonify(mensagens), 200

if __name__ == '__main__':
    # O README menciona que o teste foi feito localmente na porta 3000
    app.run(host='0.0.0.0', port=3000)
