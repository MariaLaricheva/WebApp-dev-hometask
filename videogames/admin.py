# Register your models here.

from django.contrib import admin
from .models import Games, Companies


admin.site.register(Games)

admin.site.register(Companies)