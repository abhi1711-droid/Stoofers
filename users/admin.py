from django.contrib import admin
from django.contrib.auth import get_user_model

from users.models import CustomUserModel, StoofersCard


class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'pincode', 'college_id']
    list_filter = ['id', 'phone', 'pincode', 'college_id']


admin.site.register(CustomUserModel, UserDetailsAdmin)


class StoofersAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'card_number']
    list_filter = ['id', 'name', 'card_number']


admin.site.register(StoofersCard, StoofersAdmin)
