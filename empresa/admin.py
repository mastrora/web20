from django.contrib import admin

from .models import Contacto, Foto


class ContactoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "correo", "mensaje"]
    #list_editable = ["price", "stock"]
    search_fields = ["nombre"]
    list_per_page = 30


class FotoAdmin(admin.ModelAdmin):
    list_display = ["title", "detail"]
    search_fields = ["title"]
    list_per_page = 30



admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Foto, FotoAdmin)
