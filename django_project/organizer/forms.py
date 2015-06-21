from django import forms

class UploadFileFormView(forms.Form):
    file = forms.FileField()

