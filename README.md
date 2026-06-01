# Actividad N° 4 - Manejo de Formularios con Django

## Respuestas

### 1. ¿Qué aprendiste sobre el flujo entre formulario, vista y template?
* [cite_start]**GET:** El usuario pide la página, la vista crea el formulario vacío y el template lo muestra[cite: 25].
* [cite_start]**POST:** El usuario envía los datos, la vista los recibe (`request.POST`) e inyecta al formulario[cite: 24].
* [cite_start]**Validación:** Si hay errores, la vista recarga el template con los mensajes de error[cite: 8, 26]. Si es válido, se procesan los datos limpios (`cleaned_data`).

### 2. ¿Cuál es la ventaja de usar ModelForm?
Aplica el principio **DRY** (Don't Repeat Yourself). [cite_start]En lugar de escribir el formulario campo por campo, `ModelForm` lee la estructura de un modelo de la base de datos, genera los campos automáticamente con sus validaciones y permite guardarlos directo con `.save()`[cite: 33, 40].