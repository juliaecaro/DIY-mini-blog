from django.contrib import admin
from .models import Blog, BlogAuthor, BlogComment # Importing the Models

# Register your models here.
admin.site.register(BlogAuthor)
admin.site.register(BlogComment)

# Admin site blog posts records should display the list of associated comments inline (below each blog post).
class BlogCommentsInline(admin.TabularInline):
	model = BlogComment
	max_num=0 # Stops showing empty comments

@admin.register(Blog)
# Register the admin class with the associated model
class BlogAdmin(admin.ModelAdmin):
	# Administration object for Blog models
	list_display = ('name', 'author', 'post_date')
	inlines = [BlogCommentsInline]
	list_filter = ('author', 'post_date')