from django import forms
from cluster_app.models import FichierFrom


class FichierFrom(forms.ModelForm):
     class Meta:
         model=FichierFrom
         fields="__all__"