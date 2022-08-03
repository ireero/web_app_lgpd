from django.contrib import admin
from .models import Usuario

# Registra o Objeto Usuario nas configurações de administração do Django.
admin.site.register(Usuario)
