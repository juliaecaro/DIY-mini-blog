from django.urls import path
from . import views

urlpatterns = [
  # An index page describing the site.
  path('', views.index, name='index'),
	# A page with a list of all blogs on the site
  path('blogs/', views.BlogListView.as_view(), name='blogs'),
	# Specific blog post detail pages
  path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
  # Blogger names are linked to Blog author detail pages.
  path('blogger/<int:pk>', views.BlogListbyAuthorView.as_view(), name='blogs-by-author'),
	# A page with a list of all bloggers on the site
  path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
	# A page for using the comment form to create a new comment on a blog post
  path('blog/<int:pk>/create/', views.BlogCommentCreate.as_view(), name='blog_comment'),
]
