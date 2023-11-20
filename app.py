import json
from IA_heart import detectar_cardio

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('principal.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/resultado')

def resposta():
    with open('forms.json', 'r') as arquivo:
        formulario = json.load(arquivo)

    resultado, indica = detectar_cardio([[formulario['idade'],formulario['peso'],formulario['sys_pressure'],formulario['dia_pressure'],formulario['cholesterol']]])
    print(indica)
    if(indica):
        return render_template('resultado_positivo.html')
    else:
       return  render_template('resultado_negativo.html')

@app.route('/processar', methods=['POST'])
def processar_formulario():
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
    return resposta()

if __name__ == '__main__':
    app.run(debug=True, port=9999)