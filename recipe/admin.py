from django.contrib import admin
from .models import Recipe, Rating, Ingredient, CustomUser, UserProfile
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Rating)


