from django.contrib import admin
from .models import Pet


# @admin.register(PetType)
# class PetAdmin(admin.ModelAdmin):
#     pass


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    @staticmethod
    def pet_name(obj):
        return obj.pet.name