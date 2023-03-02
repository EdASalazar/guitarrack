from django.forms import ModelForm
from .models import Restringing

class RestringingForm(ModelForm):
    class Meta:
        model = Restringing
        fields = ['date', 'string']
