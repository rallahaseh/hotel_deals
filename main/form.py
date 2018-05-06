from django import forms
from .models import Post

class HomeForm(forms.ModelForm):
    destination_name = forms.CharField(max_length=20)
    # post = forms.CharField()
    #
    class Meta:
        model = Post
        fields = ('destination_name',)
