from django.db import models
from datetime import date
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User # Blog author or commenter

# Create your models here.

# Blog posts
class Blog(models.Model):
	# Model representing a blog post.
	name = models.CharField(max_length=200)
	# Foreign Key used because blogs can only have one author/blogger, but authors can have multiple blog posts
	author = models.ForeignKey('BlogAuthor', on_delete=models.SET_NULL, null=True)
	description = models.TextField(max_length=2000, help_text="Enter the blog post's text here.")
	post_date = models.DateField(default=date.today)

	class Meta:
		# List sorted by post date (newest to oldest).
		ordering = ['-post_date']

	def get_absolute_url(self):
		# Returns the URL to access a particular blog instance.
		return reverse('blog-detail', args=[str(self.id)])

	def __str__(self):
		# String for representing the Model object.
		return self.name

# Blog post authors
class BlogAuthor(models.Model):
	# Model representing a blog author/blogger
	user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
	bio = models.TextField(max_length=400, help_text="Enter your bio details here.")

	class Meta:
		ordering = ['user', 'bio']

	def get_absolute_url(self):
		# Returns the URL to access a particular blog author instance.
		return reverse('blogs-by-author', args=[str(self.id)])

	def __str__(self):
		# String for representing the Model object.
		return self.user.username

# Blog post comments
class BlogComment(models.Model):
	# Model representing a comment written on a blog post.
	description = models.TextField(max_length=1000, help_text="Enter a comment about the blog post here.")
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	# Foreign Key used because a comment can only have one author/blogger, but authors can have multiple comments
	post_date = models.DateTimeField(auto_now_add=True)
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

	class Meta:
		# Comments should be sorted in order: oldest to most recent.
		ordering = ['post_date']

	def __str__(self):
		# String for representing the Model object.
		# Comment names in the Admin site are created by truncating the comment description to 75 characters.
		len_title=75
		if len(self.description)>len_title:
			titlestring=self.description[:len_title] + '...'
		else:
			titlestring=self.description
		return titlestring
		
		# Other types of records can use basic registration.