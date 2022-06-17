from django.db import models
#from captcha.fields import ReCaptchaField
#from captcha.widgets import ReCaptchaV2Checkbox

# Create your models here.

opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
]         

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=60)
    #tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField(max_length=700)
    #avisos = models.BooleanField(default=True)
    #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def __str__(self):
        return self.nombre


class Foto(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    detail = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Información del producto')    



    def __str__(self):
     return self.title


    class Meta:
      ordering = ['title']

