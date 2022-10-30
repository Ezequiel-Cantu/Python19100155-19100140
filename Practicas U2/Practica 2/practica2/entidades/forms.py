from django.forms import ModelForm,EmailInput,DateInput,SelectDateWidget
from entidades.models import Autor,Biblioteca,Libro,Editora

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class LibroForm(ModelForm):
    class Meta:
        model=Libro
        fields='__all__'

class BibliotecaForm(ModelForm):
    class Meta:
        model=Biblioteca
        fields='__all__'
        widgets = {
            'fechafundacion':SelectDateWidget(empty_label="Nothing")
        }
        
class EditoraForm(ModelForm):
    class Meta:
        model = Editora
        fields='__all__'