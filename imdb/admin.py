from django.contrib import admin
from imdb.models import *
# Register your models here.
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Cast)
admin.site.register(Genre)
