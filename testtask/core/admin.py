from django.contrib import admin
from .models import POI, POICategories, POIRatings

# Register your models here.
@admin.register(POI)
class POIAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    list_display = ('internal_id', 'name', 'category', 'average_rating', 'id')
    search_fields = ('internal_id', 'id')
