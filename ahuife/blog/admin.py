from django.contrib import admin

# Register your models here.

from blog.models import User,Post,Category,Tag

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
# admin.site.register(Article)