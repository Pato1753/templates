from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    data = {"nombre":"Patricio"}

    return render(request, "templatesApp/firsttemplate.html", data)

def InfoUsuario(request):
        data_us = {"ID": 123,
            "nombre":"Patricio",
            "email": "pato@gmail.com"
            }
        return render(request, "templatesApp/userInfoTemplate.html",data_us)
