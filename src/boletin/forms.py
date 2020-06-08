from django import forms

from boletin.models import Registrado


class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["nombre", "email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, provedor = email.split("@")
        dominio, extension = provedor.split(".")
        filtro = ("edu", "xxx", "com")
        if extension not in filtro:
            raise forms.ValidationError("Introduce un email con las extensiones: " + str(filtro))
        return email

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        return nombre


class ContactForm(forms.Form):
    nombre = forms.CharField(required=False)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea, min_length=20)


