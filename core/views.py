from django.shortcuts import render
from .forms import ContactoForm

def contacto_view(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)  # Binding de datos
        if form.is_valid():
            datos_recibidos = form.cleaned_data
            # Aquí se procesarían los datos de ser necesario
            return render(request, 'contacto.html', {'form': ContactoForm(), 'exito': True})
    else:
        form = ContactoForm()  # Formulario vacío para peticiones GET
        
    return render(request, 'contacto.html', {'form': form})