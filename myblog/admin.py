from django.contrib import admin
from myblog.models import Post, Category, PostAdmin, CategoryAdmin
# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
