from django.db import models
from django.conf import settings

# Modelo Sprint
class Sprint(models.Model):
    ESTADOS = (
        ('Planificado', 'Planificado'),
        ('Activo', 'Activo'),
        ('Terminado', 'Terminado'),
    )
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    objetivo = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Planificado')

    def __str__(self):
        return self.nombre

# Modelo Tarea (Historias de Usuario)
class Tarea(models.Model):
    ESTADOS = (
        ('Por Hacer', 'Por Hacer'),
        ('En Progreso', 'En Progreso'),
        ('Terminado', 'Terminado'),
    )
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Por Hacer')
    
    # Relación con el Sprint
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, related_name='tareas')
    
    # Relación con el Usuario
    responsable = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='tareas_asignadas'
    )

    def __str__(self):
        return self.titulo
    