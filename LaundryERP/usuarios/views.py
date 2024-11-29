from django.shortcuts import render, redirect
from .forms import ClienteForm, EmpleadoForm

# Create your views here.
def index_empleado(request):
    if request.method == 'POST':
        form_empleado = EmpleadoForm(request.POST)
        if form_empleado.is_valid():
            form_empleado.save()
            return redirect('index')
    else:
        form_empleado = EmpleadoForm()
    return render(request, 'usuarios/usuarios.html', {'form': form_empleado})

def index_cliente(request):
    if request.method == 'POST':
        form_cliente = ClienteForm(request.POST)
        if form_cliente.is_valid():
            form_cliente.save()
            return redirect('index')
    else:
        form_cliente = ClienteForm()
    return render(request, 'usuarios/empleados.html', {'form': form_cliente})