from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User #Blog author or commenter
from blog.models import BlogAuthor, Blog
from django.urls import reverse

# The BlogListView (all-blog page) is accessible at the expected location (e.g. /blog/blogs)
# The BlogListView (all-blog page) is accessible at the expected named URL (e.g. 'blogs')
# The BlogListView (all-blog page) uses the expected template (e.g. the default)
# The BlogListView paginates records by 5 (at least on the first page)

# Blog views tests
class BlogListView(TestCase):
	@classmethod
	# The information all Blog view tests are going to use
	def setUpTestData(cls):
		# Test User 1
		test_user1 = User.objects.create_user(username = 'testuser1', password = 'password1')
		test_user1.save()
		# Blog Authors
		blog_author = BlogAuthor.objects.create(user = test_user1, bio = "This is test_user1's bio.")

		# Creating 12 blogs
		number_of_blogs = 12
		# The 12 Blogs' Descriptions
		for blog_num in range(number_of_blogs):
			Blog.objects.create(name = 'Test Blog %s' % blog_num, author = blog_author, description = 'Test Blog %s Description' % blog_num)

	# Seeing if the BlogListView exists at the expected location
	def test_view_url_exists(self):
		resp = self.client.get('/blog/blogs/')
		self.assertEqual(resp.status_code, 200)

	# Seeing if the BlogListView exists at the expected named URL
	def test_view_url_name_accessible(self):
		resp = self.client.get(reverse('blogs'))
		self.assertEqual(resp.status_code, 200)

	# Seeing if the BlogListView uses the expected template
	def test_view_correct_template(self):
		resp = self.client.get(reverse('blogs'))
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, 'blog/blog_list.html')

	# Seeing if the BlogListView is paginated by 5
	def test_pagination(self):
		resp = self.client.get(reverse('blogs'))
		self.assertEqual(resp.status_code, 200)
		self.assertTrue('is_paginated' in resp.context)
		self.assertTrue(resp.context['is_paginated'] == True)
		self.assertEqual(len(resp.context['blog_list']), 5)