from django.shortcuts import render,get_object_or_404,redirect
from gestorapp.models import Obra,Disciplina,Escuela,Artista,Museo
from gestorapp.forms import ObraForm,DisciplinaForm,EscuelaForm,ArtistaForm,MuseoForm

# Create your views here.

###Detalles
def detalleArtista(request,id):
    artista = get_object_or_404(Artista,pk=id)
    return render(request,'detalle.html',{'entidad':artista})

def detalleMuseo(request,id):
    museo = get_object_or_404(Museo,pk=id)
    return render(request,'detalle.html',{'entidad':museo})

def detalleEscuela(request,id):
    escuela = get_object_or_404(Escuela,pk=id)
    return render(request,'detalle.html',{'entidad':escuela})

def detalleObra(request,id):
    obra = get_object_or_404(Obra,pk=id)
    return render(request,'detalle.html',{'entidad':obra})

def detalleDisciplina(request,id):
    autor = get_object_or_404(Disciplina,pk=id)
    return render(request,'detalle.html',{'entidad':autor})


###Agregar


def nuevaObra(request):
    if request.method == "POST":
        obraForm = ObraForm(request.POST)
        if obraForm.is_valid():
            obraForm.save()
            return redirect('index')
    else:
        obraForm=ObraForm()
        return render(request,'agregar.html',{'forma':obraForm})
    

def nuevaMuseo(request):
    if request.method == "POST":
        museoForm = MuseoForm(request.POST)
        if museoForm.is_valid():
            museoForm.save()
            return redirect('index')
    else:
        museoForm=MuseoForm()
        return render(request,'agregar.html',{'forma':museoForm})


def nuevaArtista(request):
    if request.method == "POST":
        artistaForm = ArtistaForm(request.POST)
        if artistaForm.is_valid():
            artistaForm.save()
            return redirect('index')
    else:
        artistaForm=ArtistaForm()
        return render(request,'agregar.html',{'forma':artistaForm})
    

def nuevaDisciplina(request):
    if request.method == "POST":
        disciplinaForm = DisciplinaForm(request.POST)
        if disciplinaForm.is_valid():
            disciplinaForm.save()
            return redirect('index')
    else:
        disciplinaForm=DisciplinaForm()
        return render(request,'agregar.html',{'forma':disciplinaForm})


def nuevaEscuela(request):
    if request.method == "POST":
        escuelaForm = EscuelaForm(request.POST)
        if escuelaForm.is_valid():
            escuelaForm.save()
            return redirect('index')
    else:
        escuelaForm=EscuelaForm()
        return render(request,'agregar.html',{'forma':escuelaForm})
    
    
###Editar

def editarObra(request,id):
    obra = get_object_or_404(Obra,pk=id)
    if request.method == "POST":
        formaObra = ObraForm(request.POST,instance=obra)
        if formaObra.is_valid():
            formaObra.save()
            return redirect('index')
    else:
        formaObra = ObraForm(instance=obra)
        return render(request,'editar.html',{'forma':formaObra})
    
def editarMuseo(request,id):
    museo = get_object_or_404(Museo,pk=id)
    if request.method == "POST":
        formaMuseo = MuseoForm(request.POST,instance=museo)
        if formaMuseo.is_valid():
            formaMuseo.save()
            return redirect('index')
    else:
        formaMuseo = MuseoForm(instance=museo)
        return render(request,'editar.html',{'forma':formaMuseo})
    
def editarDisciplina(request,id):
    disciplina = get_object_or_404(Disciplina,pk=id)
    if request.method == "POST":
        formaDisciplina = DisciplinaForm(request.POST,instance=disciplina)
        if formaDisciplina.is_valid():
            formaDisciplina.save()
            return redirect('index')
    else:
        formaDisciplina = DisciplinaForm(instance=disciplina)
        return render(request,'editar.html',{'forma':formaDisciplina})
    
def editarArtista(request,id):
    artista = get_object_or_404(Artista,pk=id)
    if request.method == "POST":
        formaArtista = ArtistaForm(request.POST,instance=artista)
        if formaArtista.is_valid():
            formaArtista.save()
            return redirect('index')
    else:
        formaArtista = ArtistaForm(instance=artista)
        return render(request,'editar.html',{'forma':formaArtista})
    
def editarEscuela(request,id):
    escuela = get_object_or_404(Escuela,pk=id)
    if request.method == "POST":
        formaEscuela = EscuelaForm(request.POST,instance=escuela)
        if formaEscuela.is_valid():
            formaEscuela.save()
            return redirect('index')
    else:
        formaEscuela = EscuelaForm(instance=escuela)
        return render(request,'editar.html',{'forma':formaEscuela})
    
    
###Eliminar

def eliminarObra(rquest,id):
    obra = get_object_or_404(Obra,pk=id)
    if obra:
        obra.delete()
    return redirect('index')

def eliminarMuseo(rquest,id):
    museo = get_object_or_404(Museo,pk=id)
    if museo:
        museo.delete()
    return redirect('index')

def eliminarArtista(rquest,id):
    artista = get_object_or_404(Artista,pk=id)
    if artista:
        artista.delete()
    return redirect('index')

def eliminarEscuela(rquest,id):
    escuela = get_object_or_404(Escuela,pk=id)
    if escuela:
        escuela.delete()
    return redirect('index')

def eliminarDisciplina(rquest,id):
    disciplina = get_object_or_404(Disciplina,pk=id)
    if disciplina:
        disciplina.delete()
    return redirect('index')