from django.contrib import admin
from blog.models import Tag, Post

# Register
admin.site.register(Tag)

# Configure how admin site behaves with models
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)