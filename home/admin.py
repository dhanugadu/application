from django.contrib import admin
from home.models import institution  , transport
from atexit import register

# Register your models here.

@admin.register(institution)
class institutionAdmin(admin.ModelAdmin):
    list_display = ['id','sname','course','fee']


@admin.register(transport)
class transportAdmin(admin.ModelAdmin):
    list_display = ['id','bus','plane','ola']
