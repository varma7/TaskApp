from django import forms
from App.models import TODOM

class TODODF(forms.ModelForm):
    class Meta:
        model = TODOM
        fields = ['title']
        widgets={
            'title':forms.TextInput(attrs={
                'class':'input-group-prepend',
                'id' : 'basic-addon1',
                'size': 40
            })
        }
        labels = {
            'title' : ('Create Task'),
        }
