from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Logs)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('status','remarks','end_time')
    
@admin.register(models.Tasks)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','report','merchant','frequency','d1','path')
    