from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Comment)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('post', 'author')
    list_display = ['author', 'post']


@admin.register(Post)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('likes',)   


@admin.register(Tag)
class ComplaintAdmin(admin.ModelAdmin):
    pass
