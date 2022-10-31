from django.forms import ModelForm
from gestorapp.models import Artista,Museo,Escuela,Disciplina,Obra

class ArtistaForm(ModelForm):
    
    class Meta:
        model = Artista
        fields = '__all__'

class MuseoForm(ModelForm):
    
    class Meta:
        model = Museo
        fields = '__all__'

class EscuelaForm(ModelForm):
    
    class Meta:
        model = Escuela
        fields = '__all__'

class DisciplinaForm(ModelForm):
    
    class Meta:
        model = Disciplina
        fields = '__all__'

class ObraForm(ModelForm):
    
    class Meta:
        model = Obra
        fields = '__all__'
