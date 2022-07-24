from django.contrib import admin

from .models import Artists,User,Songs

# Register your models here.
admin.site.register(User)
admin.site.register(Artists)
admin.site.register(Songs)
