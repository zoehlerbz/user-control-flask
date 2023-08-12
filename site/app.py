from flask import Flask, render_template, request
from src.sign_up_auth import sign_up_auth

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/auth', methods=['POST',])
def auth():
    if request.method == 'POST':
        form = request.form['form_submit']

        if form == 'submit_sign_in':

            #
            #
            # APENAS VERIFICA SE O USUÁRIO FEZ LOGIN
            # AINDA FALTA FAZER TODA A IMPLEMENTAÇÃO
            #
            #

            login_user = request.form['loginName']
            login_pass = request.form['loginPassword']

            return '<h1>sign in</h1>'

        elif form == 'submit_sign_up':

            #
            #
            # FALTA CONFERIR SE O USUÁRIO JÁ EXISTE
            # FALTA CRIPTOGRAFAR A SENHA
            # FALTA CRIAR O SISTEMA DE ENVIO DE E-MAIL E CONFIRMAÇÃO DE E-MAIL
            #
            #

            register_user = request.form['registerUsername']
            register_email = request.form['registerEmail']
            register_pass = request.form['registerPassword']
            register_repeat_pass = request.form['registerRepeatPassword']
        
            autentication = sign_up_auth(register_user, register_email, register_pass, register_repeat_pass)
            if autentication.user_registration():
                return '<h1>sign up: true</h1>'

            return '<h1>sign up: false</h1>'
        else:
            return '<h1>else</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')