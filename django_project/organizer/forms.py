from django import forms

class UploadFileFormView(forms.Form):
    file = forms.FileField(
        label="",
        widget=forms.FileInput(
            attrs={
                'class': 'form-file-input',
                'name': 'sheet'
            }
        )
    )

