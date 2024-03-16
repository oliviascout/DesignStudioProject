from django.contrib import admin
from .models import *
# Register your models here.

#class GameAdmin(admin.ModelAdmin):
#    list_display = ['name', 'release_date', 'get_publisher', 'get_platform', 'likes', 'plays']


admin.site.register(Review)
admin.site.register(Platform)
admin.site.register(Publisher)
admin.site.register(Game)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'game', 'date', 'heart')
    list_filter = ('heart', 'date')
    search_fields = ('user', 'email', 'content')
    actions = ['aprrove_comments']

    def approve_comments(self, request, queryset):
        queryset.update(heart=True)