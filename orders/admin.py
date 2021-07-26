from django.contrib import admin

from .models import User, Employer, Customer, Order


admin.site.register(User)
admin.site.register(Employer)
admin.site.register(Customer)
admin.site.register(Order)
