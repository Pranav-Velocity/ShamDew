from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Form)
admin.site.register(ProductionData)

admin.site.register(CustomerDetail)
admin.site.register(UserLog)