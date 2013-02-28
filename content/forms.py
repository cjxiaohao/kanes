from .models import Content
from django.forms import ModelForm

class WriteForm ( ModelForm ):
    class Meta:
        model = Content
