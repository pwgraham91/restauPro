from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from host_management.models import Restaurant, Table, Party

admin.site.register(Restaurant, UserAdmin)
admin.site.register(Table)
admin.site.register(Party)