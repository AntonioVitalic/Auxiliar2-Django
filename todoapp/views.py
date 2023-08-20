from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

# Create your views here.
from todoapp.models import Tarea
from categorias.models import Categoria


def tareas(request): #the index view
    """
    Los métodos de las views siempre deben recibir una request, porque ahí se encuentra la información de la request HTTP.

    En este caso, la view tendrá una variable tareas que tendrá todas las tareas de la base de datos.
    Y otra variable categorias que tendrá todas las categorías de la base de datos.

    Como estamos cargando la página, la request que la aplicación recibe es de tipo GET, y queremos que al recibir una 
    request de este tipo se haga render de la página, es decir, se muestre la página de tareas.

    El último parámetro del método render es un diccionario con toda la información que
    la view le entregará al template que vamos a cargar (que en este caso aún no existe).
    """
    mis_tareas = Tarea.objects.all()  # quering all todos with the object manager
    categorias = Categoria.objects.all()  # getting all categories with object manager

    if request.method == "GET":
        return render(request, "todoapp/index.html", {"tareas": mis_tareas, "categorias": categorias})
    """
    Es importante destacar que en el código hay una variable llamada nombre_categoria y otra llamada categoria, la primera será el valor que se envía en el formulario y corresponde al nombre de la categoría ya que así lo definimos al poner value="{{ categoria.name }}" en las opciones del form:

    <option class="" value="{{ categoria.name }}" name="{{ categoria.name }}">{{ categoria.name }}</option>

    La segunda corresponde a una instancia del modelo Categoria, que será la llave foránea de nuestra nueva Tarea.
    """
    if request.method == "POST":  # revisar si el método de la request es POST
        if "taskAdd" in request.POST:  # verificar si la request es para agregar una tarea (esto está definido en el button)
            titulo = request.POST["titulo"]  # titulo de la tarea
        
            nombre_categoria = request.POST["selector_categoria"]  # nombre de la categoria
            categoria = Categoria.objects.get(nombre=nombre_categoria)  # buscar la categoría en la base de datos
        
            contenido = request.POST["contenido"]  # contenido de la tarea
        
            nueva_tarea = Tarea(titulo=titulo, contenido=contenido, categoria=categoria)  # Crear la tarea
            nueva_tarea.save()  # guardar la tarea en la base de datos.

            return redirect("/tareas")  # recargar la página.

