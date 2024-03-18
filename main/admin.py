from django.contrib import admin
from .models import *

def set_inactive(modeladmin, request, queryset):
    queryset.update(ishdami=False)
set_inactive.short_description = 'Ishchilarni kelmaganga belgilash'


admin.ModelAdmin.actions = [set_inactive]
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('ism', 'familiya', 'ishdami', 'login', 'password')
