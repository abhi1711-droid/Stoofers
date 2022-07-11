from django.contrib import admin
from offers.models import Company, Category, Offer, Offer_Category, Offer_City


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']


admin.site.register(Company, CompanyAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']


admin.site.register(Category, CategoryAdmin)


class OfferAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'terms', 'value', 'value_type', 'company']
    list_filter = ['id', 'name', 'value', 'value_type', 'company']


admin.site.register(Offer, OfferAdmin)


class Offer_CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'offer', 'category']
    list_filter = ['id', 'offer', 'category']


admin.site.register(Offer_Category, Offer_CategoryAdmin)


class Offer_CityAdmin(admin.ModelAdmin):
    list_display = ['offer', 'city']
    list_filter = ['offer', 'city']


admin.site.register(Offer_City, Offer_CityAdmin)
