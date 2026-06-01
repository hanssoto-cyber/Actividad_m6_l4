from django.urls import path
from .views import contacto_view

urlpatterns = [
    # Al dejarlo vacío '', responderá directamente en la raíz del sitio
    path('', contacto_view, name='contacto'), 
]