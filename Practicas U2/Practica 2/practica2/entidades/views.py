from django.shortcuts import render,get_object_or_404,redirect
from entidades.models import Autor,Libro,Biblioteca,Editora
from entidades.forms import AutorForm,LibroForm,BibliotecaForm,EditoraForm

# Create your views here.

##Autor
def detalleAutor(request,id):
    autor = get_object_or_404(Autor,pk=id)
    return render(request,'detalle.html',{'entidad':autor})

def nuevaAutor(request):
    if request.method == "POST":
        autorForm = AutorForm(request.POST)
        if autorForm.is_valid():
            autorForm.save()
            return redirect('index')
    else:
        autorForm=AutorForm()
        return render(request,'agregar.html',{'forma':autorForm})
    

def editarAutor(request,id):
    autor = get_object_or_404(Autor,pk=id)
    if request.method == "POST":
        formaAutor = AutorForm(request.POST,instance=autor)
        if formaAutor.is_valid():
            formaAutor.save()
            return redirect('index')
    else:
        formaAutor = AutorForm(instance=autor)
        return render(request,'editar.html',{'forma':formaAutor})
    
def eliminarAutor(rquest,id):
    autor = get_object_or_404(Autor,pk=id)
    if autor:
        autor.delete()
    return redirect('index')

##Biblioteca
def detalleBiblioteca(request,id):
    biblioteca = get_object_or_404(Biblioteca,pk=id)
    return render(request,'detalle.html',{'entidad':biblioteca})

def nuevaBiblioteca(request):
    if request.method == "POST":
        bibliotecaForm = BibliotecaForm(request.POST)
        if bibliotecaForm.is_valid():
            bibliotecaForm.save()
            return redirect('index')
    else:
        bibliotecaForm=BibliotecaForm()
        return render(request,'agregar.html',{'forma':bibliotecaForm})
    

def editarBiblioteca(request,id):
    biblioteca = get_object_or_404(Biblioteca,pk=id)
    if request.method == "POST":
        bibliotecaForm = BibliotecaForm(request.POST,instance=biblioteca)
        if bibliotecaForm.is_valid():
            bibliotecaForm.save()
            return redirect('index')
    else:
        bibliotecaForm = BibliotecaForm(instance=biblioteca)
        return render(request,'editar.html',{'forma':bibliotecaForm})
    
def eliminarBiblioteca(rquest,id):
    biblioteca = get_object_or_404(Biblioteca,pk=id)
    if biblioteca:
        biblioteca.delete()
    return redirect('index')




##Libro
def detalleLibro(request,id):
    libro = get_object_or_404(Libro,pk=id)
    return render(request,'detalle.html',{'entidad':libro})

def nuevaLibro(request):
    if request.method == "POST":
        libroForm = LibroForm(request.POST)
        if libroForm.is_valid():
            libroForm.save()
            return redirect('index')
    else:
        libroForm=LibroForm()
        return render(request,'agregar.html',{'forma':libroForm})
    

def editarLibro(request,id):
    libro = get_object_or_404(Libro,pk=id)
    if request.method == "POST":
        libroForm = LibroForm(request.POST,instance=libro)
        if libroForm.is_valid():
            libroForm.save()
            return redirect('index')
    else:
        libroForm = LibroForm(instance=libro)
        return render(request,'editar.html',{'forma':libroForm})
    
def eliminarLibro(rquest,id):
    libro = get_object_or_404(Libro,pk=id)
    if libro:
        libro.delete()
    return redirect('index')


##Editora
def detalleEditora(request,id):
    editora = get_object_or_404(Editora,pk=id)
    return render(request,'detalle.html',{'entidad':editora})

def nuevaEditora(request):
    if request.method == "POST":
        editoraForm = EditoraForm(request.POST)
        if editoraForm.is_valid():
            editoraForm.save()
            return redirect('index')
    else:
        editoraForm=EditoraForm()
        return render(request,'agregar.html',{'forma':editoraForm})
    

def editarEditora(request,id):
    editora = get_object_or_404(Editora,pk=id)
    if request.method == "POST":
        editoraForm = EditoraForm(request.POST,instance=editora)
        if editoraForm.is_valid():
            editoraForm.save()
            return redirect('index')
    else:
        editoraForm = EditoraForm(instance=editora)
        return render(request,'editar.html',{'forma':editoraForm})
    
def eliminarEditora(rquest,id):
    editora = get_object_or_404(Editora,pk=id)
    if editora:
        editora.delete()
    return redirect('index')