from wtforms import Form
from wtforms import StringField, FloatField, PasswordField, IntegerField, EmailField
from wtforms import validators
from wtforms import RadioField, SelectMultipleField

class UserForm(Form):
    
    matricula=IntegerField('Matricula', [validators.DataRequired(message="La matricula es obligatoria")])
    
    nombre=StringField('Nombre', [validators.DataRequired(message="El campo es obligatoria")])
    
    apellido=StringField('Apellido', [validators.DataRequired(message="El campo es obligatoria")])
    
    correo=EmailField('Correo', [validators.Email(message="ingrese correo valido")])
    
class FigurasForm(Form):
    
    valor1 = FloatField('valor 1', [validators.DataRequired(message="Valor 1 si es necesari")])
    
    valor2 = FloatField('valor 2?', [validators.DataRequired(message="Valor 2 no es necesario")])
    
    
    
    
    
    
class ClientesForm(Form):
    nombre = StringField("Nombre", [validators.DataRequired(message="El campo es requerido")])
    
    telefono = StringField("Telefono",[validators.DataRequired(message="El campo es requerido")])
    
    direccion = StringField("Direccion",[validators.DataRequired(message="El campo es requerido")])
     
    tamano = RadioField('Tamaño Pizza', choices=[('chica','Chica $40'),
                                           ('mediana','Mediana $80'),
                                           ('grande','Grande $120')],
                        validators=[validators.DataRequired(message="Seleccione un tamaño")])
    ingredientes = SelectMultipleField('Ingredientes', choices=[('jamon','Jamon $10'),
                                                                ('piña','Piña $10'),
                                                                ('champiñones','Champiñones $10'),])
    cantidad = IntegerField("Numero de pizzas",
                            [validators.DataRequired(message="Ingresa la cantidad")]
                            )