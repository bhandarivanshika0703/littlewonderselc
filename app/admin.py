from django.contrib import admin
from .models import Enquiry, Contact
from django.contrib import admin
from .models import Gallery


admin.site.register(Enquiry)
admin.site.register(Contact)
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'created_at']
    list_editable = ['is_featured']