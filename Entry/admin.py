from django.contrib import admin

from .models import Comments, Posts, Categories

# Register your models here.

admin.site.register(Posts)
admin.site.register(Categories)
admin.site.register(Comments)