from django import forms
from .models import Empleado, Cliente

class EmpleadoForm(forms.ModelForm):
    ROLES = [
        ('admin' , 'Administrador'),
        ('empleado' , 'Empleado'),
    ]
    nombre = forms.CharField( max_length=1000)
    rol = forms.ChoiceField(choices=ROLES, initial='empleado')
    correo = forms.EmailField()
    
    class Meta:
        model = Empleado
        fields = ['nombre', 'rol', 'correo']

class ClienteForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=15)
    correo  = forms.EmailField()
    direccion = forms.CharField(max_length=500)
    
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'correo', 'direccion']