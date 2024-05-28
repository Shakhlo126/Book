from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', 'id',)
    list_filter = ('name', 'id',)

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Book)
admin.site.register(Order)