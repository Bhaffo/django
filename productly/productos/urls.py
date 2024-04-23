from django.urls import path
# desde la carpeta donde me encuentro importa views
from . import views

# esto es por que al usar include en el archivo de rutas
# este va a esperar que tengamos la variable urlpatterns dentro
# del archivo que le especificamos
app_name = 'productos'
urlpatterns = [
    path('', views.index, name='producto_index'),
    path('formulario', views.formulario, name='formulario'),
    path(
        '<int:producto_id>',
        views.detalle,
        name='detalle'
    ),
]
