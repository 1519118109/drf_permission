from django.contrib import admin

# Register your models here.
from permissionapp import models

admin.site.register(models.User)
