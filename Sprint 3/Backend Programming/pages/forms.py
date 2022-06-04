from django import forms

from pages.models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = [
            'f_name',
            'l_name',
            'email',
            'width',
            'height',
            'investment',
            'type',
            'details'
        ]
        widgets = {
            'f_name': forms.TextInput(attrs={
                'class': 'personal',
                'placeholder': 'first name'
            }),
            'l_name': forms.TextInput(attrs={
                'class': 'personal',
                'placeholder': 'last name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'personal',
                'placeholder': 'your email here'
            }),
            'width': forms.NumberInput(attrs={
                'placeholder': ' width in pixels/cm/in'
            }),
            'height': forms.NumberInput(attrs={
                'placeholder': 'height in pixels/cm/in'
            }),
            'type': forms.RadioSelect(attrs={
                'action': ''
            }),
            'investment': forms.NumberInput(attrs={
                'placeholder': '₱PHP'
            }),
            'details': forms.Textarea(attrs={
                'class': 'details',
                'placeholder': 'Type out specifics here.'
            })

        }
