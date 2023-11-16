from django.contrib import admin

from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass