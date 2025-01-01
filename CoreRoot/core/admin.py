from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Post

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_active', 'is_superuser', 'created', 'updated')
    list_filter = ('is_active', 'is_superuser', 'created')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('-created',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'created', 'updated')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_superuser'),
        }),
    )
    
    

class PostAdmin(admin.ModelAdmin):
    list_display = ('public_id', 'author', 'body', 'edited', 'created', 'updated')
    list_filter = ('edited', 'created', 'updated')
    search_fields = ('author__username', 'body')
    ordering = ('-created',)
    readonly_fields = ('public_id', 'created', 'updated')

    fieldsets = (
        (None, {'fields': ('public_id', 'author', 'body', 'edited')}),
        ('Important dates', {'fields': ('created', 'updated')}),
    )


# Register the User model with the modified admin class
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
