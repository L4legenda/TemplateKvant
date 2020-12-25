from .models import Person
from django.forms import ModelForm, TextInput


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['comments', 'email']

        widgets = {
            'comments': TextInput(attrs={
                'class': 'form1',
                'placeholder': 'Комментарий'
            }),
            'email': TextInput(attrs={
                'class': 'form2',
                'placeholder': 'Введите свой email'
            })

        }
