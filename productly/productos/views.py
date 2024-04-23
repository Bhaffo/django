from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Producto
from .forms import ProductoForm

# Create your views here.

# /productos


def index(request):
    # buscamos los datos de los productos
    productos = Producto.objects.all()  # .values()
    # esto nos devolvera un producto con puntaje mayor o igual a 3
    # producto = Producto.objects.filter(puntaje__gte=3)
    # esto nos devolvera un producto con puntaje igual a 3
    # producto = Producto.objects.filter(puntaje=3)
    # Para buscar un objeo especifico podemos usar id o pk(primary key)
    # producto = Producto.objects.get(id=1)

    # return JsonResponse(list(productos), safe=False)
    return render(
        request,
        'index.html',
        context={'productos': productos}
    )


def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    return render(
        request,
        'detalle.html',
        context={'producto': producto})


def formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
    else:
        form = ProductoForm()

    return render(
        request,
        'producto_form.html',
        context={'form': form}
    )
