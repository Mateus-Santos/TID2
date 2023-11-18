import json
from IA_heart import detectar_cardio

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('tela2.html')

@app.route('/processar', methods=['POST'])
def processar_formulario():
    print("OK")
    nome = request.form['nome']
    idade = int(request.form['idade'])
    sys_pressure = int(request.form['sys_pressure'])
    dia_pressure = int(request.form['dia_pressure'])
    cholesterol = int(request.form['cholesterol'])
    peso = int(request.form['peso'])

    dados = {
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "sys_pressure": sys_pressure, 
        "dia_pressure": dia_pressure,
        "cholesterol": cholesterol,
    }

    with open('forms.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)
    
    resultado, indica = detectar_cardio([[idade,peso,sys_pressure,dia_pressure,cholesterol]])

    return resultado

if __name__ == '__main__':
    app.run(debug=True, port=9999)