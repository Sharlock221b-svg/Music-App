from django.contrib import admin

from .models import Artists,User,Songs,Likes,Followers,Genre

# Register your models here.
admin.site.register(User)
admin.site.register(Artists)
admin.site.register(Songs)
admin.site.register(Likes)
admin.site.register(Followers)
admin.site.register(Genre)