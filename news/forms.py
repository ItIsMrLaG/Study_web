from .models import Information
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

# TextInput - for text
# DateTimeInput - for date + time format (2021-08-12 00:00:00)
# Textarea - for huge text

class Informatin_form(ModelForm):  # name of this class - "YOUR_MODEL_form" or thm like that
    class Meta:  # the creation of this class and its design is mandatory, as well as inheritance from the class 'ModelForm'
        model = Information
        fields = ['title', 'intro', 'full_text', 'date']  # you take this fields from your table

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of the info',
            }),
            'intro': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons',
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Main text',
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date',
            }),
        }   # creating form for taking info (it will be converted to html code + functional)
