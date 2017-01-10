from django.contrib import admin
from .models import Postt
from .models import Comentario

# Register your models here.

admin.site.register(Postt)
admin.site.register(Comentario)
