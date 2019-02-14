from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
#class Comment(models.Model):

#    title = models.CharField(max_length=100)
#    text = models.CharField(max_length=255)
#    notes = models.CharField(max_length=255)

#    def __str__(self):
#        return self.title

class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True, related_name='categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class CategoryInline(admin.TabularInline):
    model = Category.posts.through

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

    #this line is probably redundant, as I haven't included it in my list display.
    exclude = ['posts']

class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
    list_display = ['title', 'text', 'author']