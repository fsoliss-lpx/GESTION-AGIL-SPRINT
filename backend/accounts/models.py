from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Opciones para el atributo 'rol'
    ROLES = (
        ('PO', 'Product Owner'),
        ('SM', 'Scrum Master'),
        ('DEV', 'Desarrollador'),
    )
    
    # Campo adicional al modelo por defecto de Django
    rol = models.CharField(max_length=20, choices=ROLES, default='DEV')

    def __str__(self):
        return f"{self.username} - {self.get_rol_display()}"
    