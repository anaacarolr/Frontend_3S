import datetime

from flask import Flask, render_template, url_for, flash, request, redirect
from sqlalchemy.exc import SQLAlchemyError

from database import db_session, Funcionario
from sqlalchemy import select, and_, func
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '0000'

login_manager = LoginManager(app)
login_manager.login_view = 'login'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@login_manager.user_loader
def load_user(user_id):
    user = select(Funcionario).where(Funcionario.id == int(user_id))
    resultado = db_session.execute(user).scalar_one_or_none()
    return resultado


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
            flash("soma realizada", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash("preencha o campo para realizar a soma", 'alert-danger')

    return render_template("operacoes.html")


@app.route('/subtrair', methods=['GET', 'POST'])
def subtrair():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            subtrair = n1 - n2
            flash("subtração realizada", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, subtrair=subtrair)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash("preencha o campo para realizar a subtração", 'alert-danger')
    return render_template("operacoes.html")


@app.route('/multiplicar', methods=['GET', 'POST'])
def multiplicar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            multiplicar = n1 * n2
            flash("multiplicação realizada", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, multiplicar=multiplicar)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash("preencha o campo para realizar a multiplicação", 'alert-danger')
    return render_template("operacoes.html")


@app.route('/dividir', methods=['GET', 'POST'])
def dividir():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            dividir = n1 / n2
            flash("divisão realizada", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, dividir=dividir)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash("preencha o campo para realizar a divisão", 'alert-danger')
    return render_template("operacoes.html")


@app.route('/geometria')
def geometria():
    return render_template("geometria.html")


@app.route('/circulo', methods=['GET', 'POST'])
def circulo():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            area_c = 3.14 * n1 * n1
            perimetro_c = 6.28 * n1
            flash("calculo realizado", 'alert-success')
            return render_template("geometria.html", n1=n1, area_c=area_c, perimetro_c=perimetro_c)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash("O campo Lado é obrigatório! Preencha para calcular", 'alert-danger')
    return render_template("geometria.html")


@app.route('/triangulo', methods=['GET', 'POST'])
def triangulo():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            area_t = n1 * n2 / 2
            perimetro_t = n1 + n2 + n2
            flash("calculo realizado", 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, area_t=area_t, perimetro_t=perimetro_t)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash("O campo Lado é obrigatório! Preencha para calcular", 'alert-danger')
    return render_template("geometria.html")


@app.route('/quadrado', methods=['GET', 'POST'])
def quadrado():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            area_q = n1 * n2
            perimetro_q = n1 * n2
            flash("calculo realizado", 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, area_q=area_q, perimetro_q=perimetro_q)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash("O campo Lado é obrigatório! Preencha para calcular", 'alert-danger')
    return render_template("geometria.html")


@app.route('/hexagono', methods=['GET', 'POST'])
def hexagono():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])

            elevado = n1 * n1
            raiz = elevado * 0.5
            resultado = elevado * raiz
            resultado2 = resultado / 4
            hexagono = resultado2 * 6
            perimetro_h = n1 * 6
            flash("calculo realizado", 'alert-success')
            return render_template("geometria.html", n1=n1, elevado=elevado, raiz=raiz, resultado=resultado,
                                   resultado2=resultado2, hexagono=hexagono, perimetro_h=perimetro_h)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash("O campo Lado é obrigatório! Preencha para calcular", 'alert-danger')
    return render_template("geometria.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('form-email')
        senha = request.form.get('form-senha')

        if  email and senha:
            verificar_email = select(Funcionario).where(Funcionario.email == email)
            resultado_email = db_session.execute(verificar_email).scalar_one_or_none()
            if resultado_email:
                if resultado_email.check_password(senha):
                    login_user(resultado_email)
                    flash(f'Logado com sucesso!', 'success')
                    return redirect(url_for('home'))
                else:
                    flash(f'Senha incorreta!', 'danger')
                    return render_template('login.html')
            else:
                flash('Email não encontrado!')
                return redirect(url_for('login'))
        else:
            flash('Preencha os campos!', 'danger')
            return render_template('login.html')

    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('home'))


@app.route('/funcionarios')
def funcionarios():
    funcionarios_sql = select(Funcionario)
    funcionarios_resultado = db_session.execute(funcionarios_sql).scalars().all()
    return render_template("funcionarios.html", lista_funcionarios=funcionarios_resultado)

@app.route('/cadastro_funcionario', methods=['GET', 'POST'])
def cadastro_funcionario():
    if request.method == 'POST':
        nome = request.form.get('form-nome')
        data_nascimento = datetime.datetime.strptime(request.form['form-data_nascimento'],'%Y-%m-%d')
        cpf = request.form.get('form-cpf')
        email = request.form.get('form-email')
        senha = request.form.get('form-senha')
        cargo = request.form.get('form-cargo')
        salario = float(request.form.get('form-salario'))

        novo_f = Funcionario(nome=nome, data_nascimento=data_nascimento, cpf=cpf, email=email, senha=senha, cargo=cargo, salario=salario)

        try:
            db_session.add(novo_f)
            db_session.commit()
            flash(f'Funcionário {nome} cadastrado com sucesso!', 'success')
        except Exception as e:
            db_session.rollback()
            flash(f'Erro ao cadastrar funcionario', 'danger')

        return redirect(url_for('funcionarios'))

@app.route('/animais')
def animais():
    return render_template('animais.html')


if __name__ == '__main__':
    app.run(debug=True)
