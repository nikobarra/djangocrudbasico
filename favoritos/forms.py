from django import forms
from .models import Favoritos


class FavoritoModelForm(forms.ModelForm):
    class Meta:
        model = Favoritos
        fields = "__all__"
