from flask import Flask, render_template, request, redirect, url_for, flash

# Inicializando o Flask
app_Suede = Flask(__name__)
app_Suede.secret_key = 'sua_chave_secreta'  # Necessário para usar mensagens flash

# Rota principal (raiz)
@app_Suede.route('/')
def raiz():
    return render_template('index.html')

# Rota para a tela de login
@app_Suede.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        senha = request.form.get('password')  # Usar get para evitar KeyError
        if validar_senha(senha):
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('sucesso'))
        else:
            flash('A senha não atende aos requisitos!', 'error')
    return render_template('login.html')

# Rota para a página de cadastro
@app_Suede.route('/criar-conta', methods=['GET', 'POST'])
def criar_conta():
    if request.method == 'POST':
        senha = request.form.get('senha')
        confirmacao = request.form.get('confirmar_senha')
        if not senha or not confirmacao:
            flash('Preencha todos os campos!', 'error')
        elif senha != confirmacao:
            flash('As senhas não coincidem!', 'error')
        elif not validar_senha(senha):
            flash('A senha não atende aos requisitos!', 'error')
        else:
            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('login'))
    return render_template('criar_conta.html')

# Rota para a página de sucesso
@app_Suede.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

@app_Suede.route('/sobre')
def sobre():
    return render_template('sobre.html')


# Função para validar a senha
def validar_senha(senha):
    import re
    # Requisitos: 6 dígitos, 1 maiúscula, 1 número, 1 caractere especial
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$'
    return bool(re.match(pattern, senha))

# Executando o servidor
if __name__ == '__main__':
    app_Suede.run(debug=True)
