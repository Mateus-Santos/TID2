import requests
import socket

from IA_heart import detectar_cardio

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
processed_data = {}
port1 = 5000
endereco = '0.0.0.0'
host_name = socket.gethostname()
ipv4_address = socket.gethostbyname(host_name)

@app.route('/')
def principal():
    return render_template('principal.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/equipe')
def equipe():
    return render_template('quem_somos.html')

@app.route('/resultado', methods=['GET'])
def tela_resultado():
    response = requests.get(f'http://{ipv4_address}:{port1}/export_json')
    dados_json = response.json()
    resultado, indica = detectar_cardio([[dados_json.get('idade'),dados_json.get('peso'),dados_json.get('sys_pressure'),dados_json.get('dia_pressure'),dados_json.get('cholesterol')]])
    return render_template('resultado.html', resultado=resultado)

@app.route('/export_json')
def export_json():
    global processed_data
    return jsonify(processed_data)

@app.route('/processar', methods=['POST'])
def processar_formulario():
    data = request.form.to_dict()
    global processed_data
    processed_data = data
    jsonify(data), 302, {'Location': '/export_json'}
    return tela_resultado()

if __name__ == '__main__':
    app.run(port=port1, host=endereco)