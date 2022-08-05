from django.shortcuts import redirect, render
from .forms import EmpresaForm

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def crearEmpresa(request):
    if request.method == 'POST':
        empresa_form = EmpresaForm(request.POST)
        if empresa_form.is_valid():
            empresa_form.save()
            return redirect('index')
    else:
        empresa_form = EmpresaForm()
    return render(request, 'sri/crear_empresa.html', {'empresa_form':empresa_form})