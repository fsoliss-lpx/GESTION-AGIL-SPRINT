from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Registramos nuestro usuario personalizado usando la vista nativa de Django
admin.site.register(Usuario, UserAdmin)