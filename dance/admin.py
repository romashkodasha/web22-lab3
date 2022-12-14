from django.contrib import admin
from .models import Class, Purchase, User


@admin.register(Class)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ('trainer', 'id', 'price', 'place', 'descr','img')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'email', 'is_superuser', 'is_staff')


@admin.register(Purchase)
class PurchasesAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')
# Register your models here.
