from django.contrib import admin
from .models import Opinion

# Register your models here.
@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = ('user', 'booking', 'rating', 'comment')