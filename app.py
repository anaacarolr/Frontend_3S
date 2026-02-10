from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

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
            flash('soma realizada', 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash('preencha para realizar a soma', 'alert-danger')
    return render_template("operacoes.html")

@app.route('/subtrair', methods=['GET', 'POST'])
def subtrair():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            subtrair = n1 - n2
            flash('subtração realizada', 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, subtrair=subtrair)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash('preencha para realizar a soma', 'alert-danger')

    return render_template("operacoes.html")

@app.route('/multiplicar', methods=['GET', 'POST'])
def multiplicar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            multiplicar = n1 * n2
            flash('multiplicação realizada', 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, multiplicar=multiplicar)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash('preencha para realizar a multiplicação', 'alert-danger')

    return render_template("operacoes.html")

@app.route('/dividir', methods=['GET', 'POST'])
def dividir():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            dividir = n1 / n2
            flash('divisão realizada', 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, dividir=dividir)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash('preencha para realizar a divisão', 'alert-danger')

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
            flash('perimetro realizad0', 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, n3=n3, triangulo=triangulo)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash('preencha para realizar o perimetro', 'alert-danger')

    return render_template("geometria.html")

@app.route('/quadrado', methods=['GET', 'POST'])
def quadrado():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            n3 = int(request.form['form-n3'])
            n4 = int(request.form['form-n4'])
            quadrado = n1 + n2 + n3 + n4
            flash('perimetro realizad0', 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, n3=n3, n4=n4,quadrado=quadrado)
        flash('preencha para realizar o perimetro', 'alert-danger')

    return render_template("geometria.html")

@app.route('/circulo', methods=['GET', 'POST'])
def circulo():
    if request.method == 'POST':
        if request.form['form-n1'] :
            n1 = int(request.form['form-n1'])
            circulo = n1 + 6.283185307179586
            flash('perimetro realizad0', 'alert-success')
            return render_template("geometria.html", n1=n1,circulo=circulo)
        flash('preencha para realizar o perimetro', 'alert-danger')

    return render_template("geometria.html")

@app.route('/hexa', methods=['GET', 'POST'])
def hexa():
    if request.method == 'POST':
        if request.form['form-n1'] :
            n1 = int(request.form['form-n1'])
            hexa = n1 * 6
            flash('perimetro realizad0', 'alert-success')
            return render_template("geometria.html", n1=n1,hexa=hexa)
        flash('preencha para realizar o perimetro', 'alert-danger')

    return render_template("geometria.html")

@app.route('/tri', methods=['GET', 'POST'])
def tri():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            tri = n1 * n2 / 2
            flash('área realizada', 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, tri=tri)
        flash('preencha para realizar o perimetro', 'alert-danger')

    return render_template("geometria.html")

@app.route('/cir', methods=['GET', 'POST'])
def cir():
    if request.method == 'POST':
        if request.form['form-n1'] :
            n1 = int(request.form['form-n1'])
            cir = 3.14 * n1 * n1
            flash('área realizada', 'alert-success')
            return render_template("geometria.html", n1=n1, cir=cir)
        flash('preencha para realizar o perimetro', 'alert-danger')

    return render_template("geometria.html")

@app.route('/qua', methods=['GET', 'POST'])
def qua():
    if request.method == 'POST':
        if request.form['form-n1'] :
            n1 = int(request.form['form-n1'])
            qua =  n1 * n1
            flash('área realizada', 'alert-success')
            return render_template("geometria.html", n1=n1, qua=qua)
        flash('preencha para realizar o perimetro', 'alert-danger')

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
            flash('área realizada', 'alert-success')
            return render_template("geometria.html", n1=n1  ,elevado=elevado, raiz=raiz, resultado=resultado, resultado2=resultado2, hexagono=hexagono)
        flash('preencha para realizar o perimetro', 'alert-danger')

    return render_template("geometria.html")

@app.route('/funcionarios')
def funcionarios():
    return render_template("funcionario.html")


@app.route('/login')
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)