from django.contrib import admin
from .models import Finch, Sighting, House

# Register your models here.
admin.site.register(Finch)
admin.site.register(Sighting)
admin.site.register(House)