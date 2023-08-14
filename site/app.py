from flask import Flask, render_template, request
from src.sign_up_auth import sign_up_auth
from src.sign_in_auth import sign_in_auth

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

            check_user = sign_in_auth(login_user, login_pass)

            if check_user.check_login():
                return '<h1>sign in: true</h1>'

            return '<h1>sign in: false</h1>'


        elif form == 'submit_sign_up':

            #
            #
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