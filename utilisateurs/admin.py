from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel, Profil


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff', 'last_login', 'id')
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUserModel, CustomUserAdmin)
admin.site.register(Profil)
