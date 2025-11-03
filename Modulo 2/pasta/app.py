from flask import Flask , render_template, request

app = Flask(__name__)

pessoa ={
'nome': ' Gui',
'idade' : 16,
'telefone' : ' 1193222-1432'



}



@app.route('/produtos')
def boomer():
    return  render_template('app.html', pessoa=pessoa)

@app.route('/produtos')
def bumber():
    return  render_template('produtos.html', pessoa=pessoa)

alunos = []

@app.route('/', methods= ['POST','GET'])
def bamber():
    nome = request.form.get('nome')
    idade = request.form.get('idade')
    email = request.form.get('email')
    rg = request.form.get('rg')
    alunos.append({'nome': nome, 'idade': idade, 'idade': idade, 'email': email, 'rg': rg})
    return render_template('register.html', alunos=alunos)


if __name__ == '__main__':
    # debug=True para reiniciar automatico e ver erro
    app.run(debug=True, host= '127.0.0.1', port=5000)
