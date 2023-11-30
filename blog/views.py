from django.shortcuts import render

# Create your views here.

from .models import Blog, BlogAuthor, BlogComment # Importing the Models
from django.contrib.auth.models import User #Blog author or commenter

def index(request):
  # View function for home page of site.
  # Generate counts of some of the main objects
  num_blogs = Blog.objects.all().count()

  # The 'all()' is implied by default.
  num_authors = BlogAuthor.objects.count()

  # Comments made
  num_comments = BlogComment.objects.count()

  # Number of visits to this view, as counted in the session variable.
  num_visits = request.session.get('num_visits', 0)
  request.session['num_visits'] = num_visits + 1

  context = {
    'num_blogs': num_blogs,
    'num_authors': num_authors,
    'num_comments': num_comments,
    'num_visits': num_visits,
  }

  # Render the HTML template index.html with the data in the context variable
  return render(request, 'index.html', context=context)

from django.views import generic

class BlogListView(generic.ListView):
  model = Blog
  # List paginated in groups of 5 articles.
  paginate_by = 5

class BlogDetailView(generic.DetailView):
  model = Blog

class BloggerListView(generic.ListView):
	model = BlogAuthor

from django.shortcuts import get_object_or_404

class BlogListbyAuthorView(generic.ListView):
	model = Blog
	template_name = 'blog/blog_list_by_author.html'
	# Not paginated.

	def get_queryset(self):
		id = self.kwargs['pk']
		target_author = get_object_or_404(BlogAuthor, pk = id)
		return Blog.objects.filter(author=target_author)

	def get_context_data(self, **kwargs):
		context = super(BlogListbyAuthorView, self).get_context_data(**kwargs)
		context['blogger'] = get_object_or_404(BlogAuthor, pk = self.kwargs['pk'])
		return context

# For comments
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse

class BlogCommentCreate(LoginRequiredMixin, CreateView):
	# Form for making a blog comment, which requires the user to be logged in
	model = BlogComment
	fields = ['description']

	def get_context_data(self, **kwargs):
		# Getting context
		context = super(BlogCommentCreate, self).get_context_data(**kwargs)
		# Adding the blog (from the id) to the context
		context['blog'] = get_object_or_404(Blog, pk = self.kwargs['pk'])
		return context

	def form_valid(self, form):
		# Adding the author and associated blog to the form data and then setting it as valid, which saves it to the model
		form.instance.author = self.request.user
		form.instance.blog = get_object_or_404(Blog, pk = self.kwargs['pk'])
		return super(BlogCommentCreate, self).form_valid(form)

	def get_success_url(self):
		# Return to the associated blog after posting the comment
		return reverse('blog-detail', kwargs = {'pk': self.kwargs['pk']})