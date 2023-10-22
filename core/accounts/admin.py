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
        
        ('permissions', {
            'fields': (
                'is_staff','is_active','is_superuser',
            ),
        }),


        ('group permissions', {
            'fields': (
                'groups','user_permissions',
            ),
        }),

        
        ('important date', {
            'fields': (
                'last_login',
            ),
        }),

    
    )

    add_fieldsets = [
        (
            "Add user",
            {
                "classes": ["wide"],
                "fields": ["email", "password1", 'password2', ],
            },
        ),

        (
            "permissions",
            {
                "classes": ["wide"],
                "fields": ['is_staff','is_active','is_superuser', ],
            },
        ),

        (
            "group permissions",
            {
                "classes": ["wide"],
                "fields": ['groups','user_permissions', ],
            },
        ),

        
    ]



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','first_name','email',)