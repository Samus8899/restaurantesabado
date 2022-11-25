from django import forms

class FormularioEmpleados(forms.Form):

    EMPLEADOS=(
        (1,'Mesero'),
        (2,'Chef'),
        (3,'Ayudante'),
        (4,'Administrativo')
    )

    nombre=forms.CharField(
        required=True,
        max_length=20,
        label='Nombre Empleado ',
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    apellido=forms.CharField(
        required=True,
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    fotografia=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    salario=forms.CharField(
        required=True,
        max_length=20,
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'})
    )
    tipo=forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class':'form-select mb-3'}),
        choices=EMPLEADOS
    )
