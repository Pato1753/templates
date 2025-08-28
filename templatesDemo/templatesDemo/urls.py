from templatesApp.views import renderTemplate
from templatesApp.views import InfoUsuario


from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("Render/", renderTemplate),
    path("usuario/", InfoUsuario)
]
