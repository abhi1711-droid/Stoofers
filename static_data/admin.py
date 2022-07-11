from django.contrib import admin
from static_data.models import City, Country, State, College, University, Pincode


class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'display_name', 'state']
    list_filter = ['id', 'name', 'display_name', 'state']


admin.site.register(City, CityAdmin)


class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']


admin.site.register(Country, CountryAdmin)


class StateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'display_name', 'country']
    list_filter = ['id', 'name', 'display_name', 'country']


admin.site.register(State, StateAdmin)


class CollegeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'university', 'city']
    list_filter = ['id', 'name', 'university', 'city']


admin.site.register(College, CollegeAdmin)


class UniversityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city']
    list_filter = ['id', 'name', 'city']


admin.site.register(University, UniversityAdmin)


class PincodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'pincode', 'city']
    list_filter = ['id', 'pincode', 'city']


admin.site.register(Pincode, PincodeAdmin)
