from django.contrib import admin
from static_data.models import City, Country, State, College, University, Pincode
from django_admin_listfilter_dropdown.filters import DropdownFilter


class CityAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "state"]
    list_filter = [
        ("name", DropdownFilter),
    ]


admin.site.register(City, CityAdmin)


class CountryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_filter = [("name", DropdownFilter)]


admin.site.register(Country, CountryAdmin)


class StateAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "country"]
    list_filter = [
        ("name", DropdownFilter),
    ]


admin.site.register(State, StateAdmin)


class CollegeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "university", "city"]
    list_filter = [
        ("name", DropdownFilter),
    ]


admin.site.register(College, CollegeAdmin)


class UniversityAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "city"]
    list_filter = [
        ("name", DropdownFilter),
    ]


admin.site.register(University, UniversityAdmin)


class PincodeAdmin(admin.ModelAdmin):
    list_display = ["id", "pincode", "city"]
    list_filter = [
        ("pincode", DropdownFilter),
    ]


admin.site.register(Pincode, PincodeAdmin)
