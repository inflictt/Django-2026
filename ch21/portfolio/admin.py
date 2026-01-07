from django.contrib import admin
from portfolio.models import Student

# admin.site.register(Student)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('name','age','city')
    search_fields=('name','age','city')
    list_filter=('age','city')
    ordering=('age',)