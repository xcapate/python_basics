from django.contrib import admin
from .models import Posts

class PostsAdmin(admin.ModelAdmin):
    list_display=('title','author','created_at')

# Register your models here.
admin.site.register(Posts,PostsAdmin)
