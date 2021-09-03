from django.contrib import admin
from .models import Blog, Comment

admin.site.register(Blog)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'blog')
    list_filter = ('created_on',)
    search_fields = ('name', 'body')

admin.site.register(Comment, CommentAdmin)
