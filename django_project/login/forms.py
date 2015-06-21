from django import forms

class EmailFormView(forms.Form):
    email = forms.EmailField()
