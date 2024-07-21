from django.contrib import admin

from .models import Comment, Follow, Group, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group',)
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description',)
    search_fields = ('title',)
    list_filter = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'created', 'post', 'author',)
    search_fields = ('text', 'post', 'author',)
    list_filter = ('created', 'post', 'author',)


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following',)
    search_fields = ('user', 'following',)
    list_filter = ('user', 'following',)


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
