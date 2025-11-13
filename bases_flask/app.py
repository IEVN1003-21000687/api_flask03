from flask import Flask, render_template, request
 
from flask import make_response, jsonify

from datetime import datetime

import json
 
import forms
 
app = Flask(__name__)
 
 
@app.route('/')
def home():
    return "Hello, Worldl"


@app.route('/pedidos', methods=['GET', 'POST'])
def pedidos():
    form = forms.ClientesForm(request.form)
    pedido = []
    ventas = []
    total_dia = 0

    pedido_cookie = request.cookies.get('pedido')
    ventas_cookie = request.cookies.get('ventas')

    if pedido_cookie:
        try:
            pedido = json.loads(pedido_cookie)
        except:
            pedido = []

    if ventas_cookie:
        try:
            ventas = json.loads(ventas_cookie)
        except:
            ventas = []

    if request.method == 'POST':
        accion = request.form.get('action')
        
        if accion == 'agregar' and form.validate():
            nombre = form.nombre.data
            direccion = form.direccion.data
            telefono = form.telefono.data
            tamano = form.tamano.data
            ingredientes = form.ingredientes.data
            cantidad = form.cantidad.data

            precios = {'chica': 40, 'mediana': 80, 'grande': 120}
            subtotal = precios[tamano] * cantidad + (10 * len(ingredientes))

            nueva_pizza = {
                'tamano': tamano,
                'ingredientes': ingredientes,
                'cantidad': cantidad,
                'subtotal': subtotal
            }

            pedido.append(nueva_pizza)
        
        elif accion and accion.startswith('quitar_'):
            try:
                indice = int(accion.split('_')[1])
                if 0 <= indice < len(pedido):
                    pedido.pop(indice)
                    print(f"Pizza eliminada en índice {indice}")
            except Exception as e:
                print("Error al eliminar:", e)

       
        elif accion == 'terminar':
            pedido_cookie = request.cookies.get('pedido')
            if pedido_cookie:
                pedido = json.loads(pedido_cookie)
                print("Pedido cargado de cookie:", pedido)
            else:
                print("No hay cookie de pedido")

            if pedido:
                total_cliente = sum(p['subtotal'] for p in pedido)
                nombre = form.nombre.data or "Cliente sin nombre"
                direccion = form.direccion.data or "Sin direccion"
                telefono = form.telefono.data or "Sin telefono"
                fecha = datetime.now().strftime('%d-%m-%Y')

                venta = {
                    'nombre': nombre,
                    'direccion': direccion,
                    'telefono': telefono,
                    'fecha': fecha,
                    'total': total_cliente
                }

                print("Venta creada:", venta)
                ventas.append(venta)
                pedido = []
            else:
                print("Pedido vacío, no se registró venta.")

 
    
    hoy = datetime.now().strftime('%d-%m-%Y')
    ventas_hoy = []
    total_dia = 0

    for v in ventas:
        if v.get('fecha') == hoy:
            ventas_hoy.append((v.get('nombre', 'Cliente'), v.get('total', 0)))
            total_dia += v.get('total', 0)

    response = make_response(render_template(
        'pedidos.html',
        form=form,
        pedido=pedido,
        ventas=ventas,
        ventas_hoy=ventas_hoy,
        total_dia=total_dia
    ))
    
    response.set_cookie('pedido', json.dumps(pedido))
    response.set_cookie('ventas', json.dumps(ventas))
    print("Cookies actualizadas con:", {'pedido': pedido, 'ventas': ventas})

    return response

@app.route("/get_cookie")
def get_cookie():
    ventas_cookie = request.cookies.get('ventas')
    if not ventas_cookie:
        return jsonify([])

    try:
        ventas = json.loads(ventas_cookie)
    except Exception as e:
        print("Error leyendo ventas:", e)
        ventas = []

    return jsonify(ventas)



















 
@app.route("/alumnos", methods=['GET','POST'])
def alumnos():
    mat=0
    nom=""
    ape=""
    em=""
    estudiantes=[] 
    tem=[]
    datos={} 
 
 
    alumnos_clase=forms.UserForm(request.form)
    if request.method=='POST' and alumnos_clase.validate():
        mat=alumnos_clase.matricula.data
        nom=alumnos_clase.nombre.data
        ape=alumnos_clase.apellido.data
        em=alumnos_clase.correo.data
        datos={"matricula":mat,"nombre":nom,"apellido":ape,"correo":em}
 
        datos_str=request.cookies.get('estudiante')
        if not datos_str:
            return "No hay cookie"
        tem=json.loads(datos_str)
        estudiantes=tem
        print(type(estudiantes))
        estudiantes.append(datos)
 
    response=make_response(render_template('Alumnos.html', form=alumnos_clase, mat=mat, nom=nom, ape=ape, em=em))
 
    response.set_cookie('estudiante',json.dumps(estudiantes))
 
    return response
 

 
@app.route('/index')
def index():
    titulo="IEVN1003 - PWA"
    listado=["Opera 1","Opera 2", "Opera 3", "Opera 4"]
    return render_template('index.html', titulo=titulo, listado=listado)
 
 
@app.route('/operas',methods=['GET','POST'])
def operas():
 
    if request.method=='POST':
        x1=request.form.get('x1')
        x2=request.form.get('x2')
        resultado=x1+x2
        return render_template('operas.html', resultado=resultado)
 
 
    return render_template('operas.html')
   
 
@app.route('/distancia')
def distancia():
    return render_template('distancia.html')
 
 
@app.route('/about')
def about():
    return "<h1>This is the about page.<h1>"
 
@app.route('/user/<string:user>')
def user(user):
    return "Hola" + user
 
@app.route('/numero/<int:n>')
def numero(n):
    return "Numero: {}".format(n)
 
@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return "ID: {} nombre {}".format(id,username)
 
@app.route("/suma/<float:n1>/<float:n2>")
def func(n1,n2):
    return "La suma es: {}".format(n1+n2)
 
@app.route("/prueba")
def prueba():
    return '''
    <h1>Prueba de HTML</h1>
    <p>Esto es un parrafo</p>
    <ul>
        <li>Elemento 1</li>
        <li>Elemento 2</li>
        <li>Elemento 3</li>
    </ul>
 
    '''
 
 
if __name__ == '__main__':
    app.run(debug=True)