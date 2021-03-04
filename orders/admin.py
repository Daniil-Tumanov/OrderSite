from django.contrib import admin
from .models import Category, Orders, Status, Users
# Register your models here.

admin.site.register(Category)
admin.site.register(Orders)
admin.site.register(Status)
admin.site.register(Users)