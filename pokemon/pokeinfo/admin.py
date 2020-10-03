from django.contrib import admin
from .models import pokemon, basestats, evolutions

# Register your models here.

admin.site.register(pokemon)
admin.site.register(basestats)
admin.site.register(evolutions)