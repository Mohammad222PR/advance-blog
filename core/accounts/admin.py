from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email','is_staff','is_active','is_superuser')
    list_filter = ('is_active','is_staff','is_superuser')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        ('Authentication', {
            'fields': (
                'email','password'
            ),
        }),
        
        ('Permisons', {
            'fields': (
                'is_staff','is_active','is_superuser',
            ),
        }),
    
    )

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password1", 'password2','is_staff','is_active','is_superuser', ],
            },
        ),
    ]



