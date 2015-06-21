from django import forms

class EmailFormView(forms.Form):
    email = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email Address',
                'spellcheck': 'false'
            }
        )
    )
