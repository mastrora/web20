from django import forms
from .models import Contacto
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox





class ContactoForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = Contacto
        
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
        