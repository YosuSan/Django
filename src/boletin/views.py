from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import RegModelForm, ContactForm
from .models import Registrado


# Create your views here.


def inicio(request):
    titulo = "HOLA"
    if request.user.is_authenticated:
        titulo = "Bienvenido %s" % request.user
    form = RegModelForm(request.POST or None)

    context = {
        "titulo": titulo,
        "form": form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        nombre = form.cleaned_data.get("nombre")
        email = form.cleaned_data.get("email")
        if not nombre:
            nombre = "Nombre por defecto"
            instance.nombre = nombre
        instance.save()
        print(instance)
        print(instance.timestamp)
        context = {
            "titulo": "Gracias %s!" % nombre,
        }

        # form_data = form.cleaned_data
        # nombre = form_data.get("nombre")
        # email = form_data.get("email")
        # print("Todo form", form_data)
        # print("Nombre", nombre)
        # print("Email:", email)
        # obj = Registrado.objects.create(email=email, nombre=nombre)

    return render(request, "inicio.html", context)


def contacto(request):
    titulo = "Contacto"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key in form.cleaned_data:
        #     print(key, ":", form.cleaned_data.get(key))
        email = form.cleaned_data.get("email")
        mensaje = form.cleaned_data.get("mensaje")
        nombre = form.cleaned_data.get("nombre")
        asunto = "Form de contacto"
        if settings.EMAIL_HOST_USER != "xxx@xxx.xxx":
            email_from = settings.EMAIL_HOST_USER
            email_to = [email_from, "otro@correo.pepino"]
            email_mensaje = "%s:\n%s \nEnviado por %s" % (nombre, mensaje, email)
            send_mail(asunto,
                      email_mensaje,
                      email_from,
                      email_to,
                      fail_silently=True
                      )
        else:
            print(email, nombre, mensaje)
    context = {
        "form": form,
        "titulo": titulo,
    }

    return render(request, "forms.html", context)
