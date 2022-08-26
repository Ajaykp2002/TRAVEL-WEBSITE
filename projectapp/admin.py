from django.contrib import admin

# Register your models here.
from projectapp.models import place
from projectapp.models import Team

admin.site.register(place)
admin.site.register(Team)