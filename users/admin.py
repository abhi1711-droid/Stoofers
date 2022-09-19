from django.contrib import admin
from users.models import CustomUserModel, StoofersCard
from django_admin_listfilter_dropdown.filters import DropdownFilter


class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ["id", "phone", "pincode", "user"]

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(CustomUserModel, UserDetailsAdmin)


class StoofersAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "card_number", "user"]

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(StoofersCard, StoofersAdmin)
