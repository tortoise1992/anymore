from django.contrib import admin

# Register your models here.

from blog.models import User,Article

admin.site.register(User)
admin.site.register(Article)