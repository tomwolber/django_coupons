from django.contrib import admin
from apps.companies.models import Company

class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name'] }	

admin.site.register(Company, CompanyAdmin,)
