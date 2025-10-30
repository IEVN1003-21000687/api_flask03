from wtforms import Form
from wtforms import StringField, FloatField, PasswordField, IntegerField, EmailField
from wtforms import validators

class UserForm(Form):
    
    matricula=IntegerField('Matricula', [validators.DataRequired(message="La matricula es obligatoria")])
    
    nombre=StringField('Nombre', [validators.DataRequired(message="El campo es obligatoria")])
    
    apellido=StringField('Apellido', [validators.DataRequired(message="El campo es obligatoria")])
    
    correo=EmailField('Correo', [validators.Email(message="ingrese correo valido")])
    
class FigurasForm(Form):
    
    valor1 = FloatField('valor 1', [validators.DataRequired(message="Valor 1 si es necesari")])
    
    valor2 = FloatField('valor 2?', [validators.DataRequired(message="Valor 2 no es necesario")])