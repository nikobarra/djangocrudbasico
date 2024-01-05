from django.shortcuts import render, redirect
from .models import Favoritos
from .forms import FavoritoModelForm
from django.urls import reverse


def index_favoritos(request):
    favoritos_lista = Favoritos.objects.all()
    context = {"favoritos_lista": favoritos_lista}

    return render(request, "favoritos/lista.html", context)


def crear_favoritos(request):
    formulario = FavoritoModelForm()

    if request.method == "POST":
        formulario = FavoritoModelForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            print(formulario.errors)

    context = {"form": formulario, "titulo": "Agregar favorito"}
    # return redirect("app_favoritos:index")
    return render(request, "favoritos/crear.html", context)


def borrar_favoritos(request, pk):
    Favoritos.objects.get(pk=pk).delete()
    return redirect("app_favoritos:index")


def detalle_favoritos(request, pk):
    favorito = Favoritos.objects.get(pk=pk)
    context = {"fav": favorito}
    return render(request, "favoritos\detalle.html", context)


def actualizar_favoritos(request, pk):
    favorito = Favoritos.objects.get(pk=pk)
    formulario = FavoritoModelForm(instance=favorito)

    if request.method == "POST":
        formulario = FavoritoModelForm(request.POST, instance=favorito)
        if formulario.is_valid():
            formulario.save()
        else:
            print(formulario.errors)

    context = {"form": formulario, "titulo": "Actualizar favorito"}

    # return redirect("app_favoritos:index")
    return render(request, "favoritos/crear.html", context)
