# Guía de Inicialización y Desarrollo: Proyecto Django Formularios

Este documento contiene el paso a paso detallado para configurar el entorno virtual, instalar las dependencias, estructurar la aplicación y subir el proyecto a GitHub para la **Actividad N° 4 - Creación y Manejo de Formularios con Django**.

---

## 1. Configuración del Entorno Virtual (Windows PowerShell)

Para evitar bloqueos con las herramientas de instalación en versiones recientes de Python, creamos un entorno limpio y forzamos la configuración de `pip` manualmente:

```powershell
# 1. Crear el entorno virtual omitiendo pip para evitar congelamientos
python -m venv .venv --without-pip

# 2. Activar el entorno virtual en la terminal (Verás el prefijo '(.venv)')
.venv\Scripts\Activate.ps1

# 3. Instalar y configurar pip de forma manual y segura
python -m ensurepip --default-pip
2. Instalación de Django e Inicialización del Proyecto
Con el entorno activo, instalamos el framework y generamos la estructura de archivos base:

PowerShell
# 1. Instalar Django en el entorno virtual
pip install django

# 2. Crear el proyecto en la raíz actual (El '.' final evita que se cree una carpeta duplicada)
django-admin startproject actividad_m6_14 .

# 3. Crear la aplicación interna para manejar el formulario de contacto
python manage.py startapp core

#Configuración Obligatoria en (settings.py)
Abre el archivo actividad_m6_14/settings.py e integra tu nueva app en la lista de aplicaciones instaladas:

Python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # <-- Tu app registrada aquí
]
3. Base de Datos y Gestión de Dependencias
Ejecutamos las migraciones del sistema para crear el archivo de base de datos local y congelamos las dependencias actuales para cumplir con las buenas prácticas de desarrollo:

PowerShell
# 1. Ejecutar las migraciones iniciales de Django (Creará el archivo db.sqlite3)
python manage.py migrate

# 2. Generar el archivo requirements.txt automáticamente con la versión de Django instalada
pip freeze > requirements.txt
4. Desarrollo del Formulario, Vistas y Plantillas
Crea y modifica los siguientes archivos dentro de la carpeta core/ para implementar la lógica solicitada:

A. El Formulario (core/forms.py)
Define los campos y agrega la validación de un mínimo de 10 caracteres para el mensaje:

Python
from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100, 
        label="Nombre",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'})
    )
    correo = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@correo.com'})
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escribe tu mensaje...'}),
        min_length=10,  # Validación requerida por el encargo
        label="Mensaje"
    )
B. La Vista (core/views.py)
Procesa el formulario capturando el envío mediante el método POST:

Python
from django.shortcuts import render
from .forms import ContactoForm

def contacto_view(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)  # Vinculación de datos (Binding)
        if form.is_valid():
            datos_recibidos = form.cleaned_data
            # Renderiza el formulario limpio y activa la bandera de éxito
            return render(request, 'contacto.html', {'form': ContactoForm(), 'exito': True})
    else:
        form = ContactoForm()  # Instancia vacía para peticiones GET
        
    return render(request, 'contacto.html', {'form': form})
C. Plantilla Base (core/templates/base.html)
Define la estructura HTML global reutilizable:

HTML
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Mi Sitio Django{% endblock %}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; }
        .container { max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .form-group { margin-bottom: 15px; }
        .errorlist { color: red; list-style-type: none; padding: 0; font-size: 0.9em; }
        .success-msg { color: green; font-weight: bold; margin-bottom: 15px; }
        button { background-color: #007bff; color: white; border: none; padding: 10px 15px; border-radius: 4px; cursor: pointer; }
        button:hover { background-color: #0056b3; }
    </style>
</head>
<body>
    <div class="container">
        {% block content %}
        {% endblock %}
    </div>
</body>
</html>
D. Plantilla del Formulario (core/templates/contacto.html)
Hereda de la base y recorre los campos imprimiendo los errores de validación de backend debajo de cada uno:

HTML
{% extends "base.html" %}

{% block title %}Contacto{% endblock %}

{% block content %}
    <h2>Formulario de Contacto</h2>

    {% if exito %}
        <p class="success-msg">¡El formulario se envió y validó correctamente!</p>
    {% endif %}

    <form method="POST" novalidate>
        {% csrf_token %}

        {% for field in form %}
            <div class="form-group">
                <label for="{{ field.id_for_label }}">{{ field.label }}</label>
                {{ field }}
                
                {% if field.errors %}
                    <ul class="errorlist">
                        {% for error in field.errors %}
                            <li>{{ error }}</li>
                        {% endfor %}
                    </ul>
                {% endif %}
            </div>
        {% endfor %}

        <button type="submit">Enviar Mensaje</button>
    </form>
{% endblock %}
E. Configuración de Rutas (urls.py)
Crea el archivo core/urls.py para conectar la vista en la raíz:

Python
from django.urls import path
from .views import contacto_view

urlpatterns = [
    path('', contacto_view, name='contacto'),  # Mapeado directamente a [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
]
Y actualiza el archivo de rutas principal actividad_m6_14/urls.py:

Python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Vincula las URLs de la app core
]
5. Control de Versiones (Git & GitHub)
Una vez verificado el funcionamiento del código, guardamos los cambios locales y actualizamos el repositorio remoto:

PowerShell
# 1. Rastrear todos los archivos nuevos y modificaciones
git add .

# 2. Confirmar los cambios con su respectivo mensaje descriptivo (-m)
git commit -m "Estructura completa de proyecto, app core y manejo de formularios"

# 3. Subir los cambios a la rama activa de tu repositorio en GitHub
git push
6. Ejecución del Servidor de Desarrollo
Para levantar la aplicación localmente y realizar pruebas de interfaz:

PowerShell
python manage.py runserver
Acceso local: http://127.0.0.1:8000/