from django.contrib import admin
from . models import NewRegister
# Register your models here.

class NewRegisterAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(NewRegister, NewRegisterAdmin)
