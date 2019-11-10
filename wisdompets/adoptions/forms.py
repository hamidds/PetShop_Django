
from django.forms import ModelForm
from .models import Pet

class UserModelForm(ModelForm):
    class Meta:
        model = Pet
        fields = ['name','species','breed','age','sex','submission_date','description']
