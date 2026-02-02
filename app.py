from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/calculos')
def calculos():
    return render_template("calculos.html")

@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")

@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            soma = n1 + n2
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)

    return render_template("operacoes.html")

@app.route('/subtrair', methods=['GET', 'POST'])
def subtrair():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            subtrair = n1 - n2
            return render_template("operacoes.html", n1=n1, n2=n2, subtrair=subtrair)

    return render_template("operacoes.html")

@app.route('/multiplicar', methods=['GET', 'POST'])
def multiplicar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            multiplicar = n1 * n2
            return render_template("operacoes.html", n1=n1, n2=n2, multiplicar=multiplicar)

    return render_template("operacoes.html")

@app.route('/dividir', methods=['GET', 'POST'])
def dividir():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            dividir = n1 / n2
            return render_template("operacoes.html", n1=n1, n2=n2, dividir=dividir)

    return render_template("operacoes.html")

@app.route('/geometria')
def geometria():
    return render_template("geometria.html")

@app.route('/triangulo', methods=['GET', 'POST'])
def triangulo():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            n3 = int(request.form['form-n3'])
            triangulo = n1 + n2 + n3
            return render_template("geometria.html", n1=n1, n2=n2, n3=n3, triangulo=triangulo)

    return render_template("operacoes.html")

@app.route('/quadrado', methods=['GET', 'POST'])
def quadrado():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            n3 = int(request.form['form-n3'])
            n4 = int(request.form['form-n4'])
            quadrado = n1 + n2 + n3 + n4
            return render_template("geometria.html", n1=n1, n2=n2, n3=n3, n4=n4,quadrado=quadrado)

    return render_template("geometria.html")

@app.route('/circulo', methods=['GET', 'POST'])
def circulo():
    if request.method == 'POST':
        if request.form['form-n1'] :
            n1 = int(request.form['form-n1'])
            circulo = n1 + 6.283185307179586
            return render_template("geometria.html", n1=n1,circulo=circulo)

    return render_template("geometria.html")

@app.route('/hexa', methods=['GET', 'POST'])
def hexa():
    if request.method == 'POST':
        if request.form['form-n1'] :
            n1 = int(request.form['form-n1'])
            hexa = n1 * 6
            return render_template("geometria.html", n1=n1,hexa=hexa)

    return render_template("geometria.html")

@app.route('/tri', methods=['GET', 'POST'])
def tri():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            tri = n1 * n2 / 2
            return render_template("geometria.html", n1=n1, n2=n2, tri=tri)

    return render_template("geometria.html")

@app.route('/cir', methods=['GET', 'POST'])
def cir():
    if request.method == 'POST':
        if request.form['form-n1'] :
            n1 = int(request.form['form-n1'])
            cir = 3.14 * n1 * n1
            return render_template("geometria.html", n1=n1, cir=cir)

    return render_template("geometria.html")

@app.route('/qua', methods=['GET', 'POST'])
def qua():
    if request.method == 'POST':
        if request.form['form-n1'] :
            n1 = int(request.form['form-n1'])
            qua =  n1 * n1
            return render_template("geometria.html", n1=n1, qua=qua)

    return render_template("geometria.html")

@app.route('/hexagono', methods=['GET', 'POST'])
def hexagono():
    if request.method == 'POST':
        if request.form['form-n1'] :
            n1 = int(request.form['form-n1'])


            elevado =  n1 * n1
            raiz = elevado * 0.5
            resultado = elevado * raiz
            resultado2 =resultado / 4
            hexagono = resultado2 * 6
            return render_template("geometria.html", n1=n1,elevado=elevado, raiz=raiz, resultado=resultado, resultado2=resultado2, hexagono=hexagono)

    return render_template("geometria.html")




#TODO Final do código

if __name__ == '__main__':
    app.run(debug=True)