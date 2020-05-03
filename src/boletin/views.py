from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import RegModelForm, ContactForm


# Create your views here.


def inicio(request):
    titulo = "Esto es un titulo generado desde python"
    if request.user.is_authenticated:
        titulo = "Bienvenido %s" % (request.user)
    form = RegModelForm(request.POST or None)

    context = {
        "el_titulo": titulo,
        "el_form": form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        nombre = form.cleaned_data.get("nombre")
        email = form.cleaned_data.get("email")
        if not nombre:
            instance.nombre = "Persona"
        instance.save()
        if not nombre:
            nombre = "persona sin nombre"
        context = {
            "el_titulo": "Gracias %s" % (nombre),
        }
    return render(request, "inicio.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key, value in form.cleaned_data.items():
        #     print(key, ":", value)
        # for key in form.cleaned_data:
        #     print(key, ":", form.cleaned_data.get(key))
        form_email = form.cleaned_data.get("email")
        form_nombre = form.cleaned_data.get("nombre")
        form_mensaje = form.cleaned_data.get("mensaje")
        asunto = "Form de contacto"
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from]
        email_mensaje = "%s: %s enviado por %s" % (form_nombre, form_mensaje, form_email)
        send_mail(asunto,
                  email_mensaje,
                  email_from,
                  email_to,
                  fail_silently=False)
    context = {
        "el_form": form,
    }

    return render(request, "forms.html", context)
