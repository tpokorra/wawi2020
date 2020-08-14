from django.contrib import admin

# Register your models here.
from .models import Location
from .models import Item

admin.site.register(Location)
admin.site.register(Item)
