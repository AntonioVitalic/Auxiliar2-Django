from django.contrib import admin

# Register your models here.
from todoapp.models import  Tarea

admin.site.register(Tarea)
#En la consola hacer: python manage.py createsuperuser y crear un superusarix 
# que podrá acceder al panel de administrador y editar elementos de la base de datos.
# Finalmente correr la aplicación web y entrar a 127.0.0.1:8000/admin y loguearse con la cuenta recién creada.