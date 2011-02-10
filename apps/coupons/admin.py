from django.contrib import admin
from apps.coupons.models import Coupon

class CouponAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name'] }	

admin.site.register(Coupon, CouponAdmin,)
