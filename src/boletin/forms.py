from django import forms

from boletin.models import Registrado


class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ("nombre", "email",)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        allowed_extension = ("edu", "xxx")

        email_base, proveeder = email.split("@")
        dominio, extension = proveeder.split(".")

        if extension not in allowed_extension:
            raise forms.ValidationError(
                "Solo válido los correos pertenecientes a las extensiones " + str(allowed_extension))
        return email

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if nombre:
            for i in nombre:
                if str(i).isnumeric():
                    raise forms.ValidationError("Los nombres no pueden contener números")
        return nombre


class ContactForm(forms.Form):
    nombre = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control form-control"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': "form-control form-control"}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))

    def clean_mensaje(self):
        mensaje = self.cleaned_data.get("mensaje")
        if len(mensaje) < 20:
            raise forms.ValidationError("El mensaje ha de contener más de 20 caracteres")
        return mensaje
