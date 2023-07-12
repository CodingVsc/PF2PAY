from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'username', 'is_active', 'is_staff',
                    'is_superuser', 'date_joined', 'last_login',
                    'is_seller', 'phone', 'balance', 'product_count']
    ordering = ('email',)


admin.site.register(User, UserAdmin)