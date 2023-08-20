from django.db import models

# Create your models here.
from django.utils import timezone
from categorias.models import Categoria

class Tarea(models.Model):  # Todolist able name that inherits models.Model
    """
    La clase Tarea hereda de models.Model para tener todas las características de un model de Django.

    El atributo título será un CharField con un largo máximo de 250 caracteres. Aquí hay mas información sobre Fields.

    En este modelo utilizamos atributos de diferentes tipos como texto y fechas.

    La variable blank=True en el atributo contenido indica que este atributo puede estar en blanco.

    La variable default = ... en el atributo fecha_creacion indica que si no se entrega una fecha de creación, por defecto se pondrá la fecha actual.

    Para crear una llave foránea utilizamos models.ForeignKey y hay que entregar el modelo que será la llave foránea y una opción de on_delete. Información sobre on_delete

    El método _ _ str_ _ permite definir cómo se mostrará una categoría al imprmirla.
    """
    titulo = models.CharField(max_length=250)  # un varchar
    contenido = models.TextField(blank=True)  # un text
    fecha_creación = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # un date
    categoria = models.ForeignKey(Categoria, default="general", on_delete=models.CASCADE)  # la llave foránea

    def __str__(self):
        return self.titulo  # name to be shown when called
    
