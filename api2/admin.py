from django.contrib import admin

from .models import studnt

# Register your models here.

@admin.register(studnt)
class studntAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']


