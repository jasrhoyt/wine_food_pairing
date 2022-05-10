from django.contrib import admin

# Register your models here.
from .models import Red_Wines, White_Wines

admin.site.register(Red_Wines)
admin.site.register(White_Wines)
