from django import forms
from .models import Empresa, DatosEmpresa

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa 
        fields = ['nombre'] 