from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world!"

@app.route('/index')
def index():
    
    titulo="IEVN1003 - PWA"
    listado =["Opera 1", "Opera 2", "Opera 3", "Opera 4"]
    
    return render_template('index.html', titulo = titulo, listado = listado)



@app.route('/about')
def about():
    return "<h1>Esta es la pagina sobre mi.</h1>"

@app.route("/user/<string:user>")
def user(user):
    return "Hola " + user

@app.route("/user/<int:n>")
def numero (n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def func1 (id,username):
    return "ID: {} nombre: {}".format(id,username)

@app.route("/suma/<float:n1>/<float:n2>")
def func2(n1,n2):
    return "La suma es de: {}".format(n1+n2)

@app.route("/prueba")
def func3():
    return """

    <h1>Prueba de HTML</h1>

"""

@app.route('/operas', methods=['GET', 'POST'])
def operas():
    
    if request.method=='POST':
        x1=request.form.get('x1')
        x2=request.form.get('x2')
        resultado=x1+x2
        return render_template('operas.html', resultado=resultado)
        
    return render_template('operas.html')

@app.route('/distancias')
def distancias():
    return render_template('distancias.html')
    

if __name__ == '__main__':
    app.run(debug=True)
    
    