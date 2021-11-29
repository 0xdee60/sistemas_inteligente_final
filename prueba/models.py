from django.db import models

# Create your models here.
class Prueba(models.Model):
    paciente = models.CharField(max_length=500, blank=False)
    fecha_nacimiento = models.DateField()
    respuesta1 = models.CharField(max_length=500, blank=False)
    respuesta2 = models.CharField(max_length=500, blank=False)
    respuesta3 = models.CharField(max_length=500, blank=False)
    respuesta4 = models.CharField(max_length=500, blank=False)
    respuesta5 = models.CharField(max_length=500, blank=False)
    respuesta6 = models.CharField(max_length=500, blank=False)
    respuesta7 = models.CharField(max_length=500, blank=False)
    respuesta8 = models.CharField(max_length=500, blank=False)
    respuesta9 = models.CharField(max_length=500, blank=False)
    respuesta10 = models.CharField(max_length=500, blank=False)
    respuesta11 = models.CharField(max_length=500, blank=False)
    respuesta12 = models.CharField(max_length=500, blank=False)
    respuesta13= models.CharField(max_length=500, blank=False)
    respuesta14 = models.CharField(max_length=500, blank=False)
    respuesta15 = models.CharField(max_length=500, blank=False)
    respuesta16 = models.CharField(max_length=500, blank=False)
    respuesta17 = models.CharField(max_length=500, blank=False)
    respuesta18 = models.CharField(max_length=500, blank=False)
    respuesta19 = models.CharField(max_length=500, blank=False)
    respuesta20 = models.CharField(max_length=500, blank=False)

    respuesta_hora = models.DateTimeField(auto_now_add=True)

    respuesta_video = models.FileField(upload_to='videos/respuestas')

    respuesta_emociones = models.CharField(max_length=1000)


    class Meta: 
        verbose_name = 'prueba'
        verbose_name_plural = 'pruebas'

    def __str__(self) -> str:
        return self.paciente