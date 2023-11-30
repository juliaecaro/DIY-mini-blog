from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User #Blog author or commenter
from blog.models import BlogAuthor, Blog, BlogComment
import datetime

# All model fields have the correct label and length.
# All models have the expected object name (e.g. __str__() returns the expected value).
# Models have the expected URL for individual Blog and Comment records (e.g. get_absolute_url() returns the expected URL).

# Blog model tests
class BlogModelTest(TestCase):
	@classmethod
	# The information all Blog model tests are going to use
	def setUpTestData(cls):
		# Test User 1
		test_user1 = User.objects.create_user(username = 'testuser1', password = 'password1')
		test_user1.save()
		# The Blog Author and Blog Author's Bio
		blog_author = BlogAuthor.objects.create(user = test_user1, bio = "This is test_user1's bio.")
		# The Test Blog Post
		blog = Blog.objects.create(name = 'Test Blog 1', author = blog_author, description = 'Test Blog 1 Description')

	# Testing the name label of the Blog model
	def test_name_label(self):
		blog = Blog.objects.get(id = 1)
		field_label = blog._meta.get_field('name').verbose_name
		self.assertEquals(field_label, 'name')

	# Testing the name length of the Blog model
	def test_name_max_length(self):
		blog = Blog.objects.get(id = 1)
		max_length = blog._meta.get_field('name').max_length
		self.assertEquals(max_length, 200)

	# Testing the description label of the Blog model
	def test_description_label(self):
		blog = Blog.objects.get(id = 1)
		field_label = blog._meta.get_field('description').verbose_name
		self.assertEquals(field_label, 'description')

	# Testing the description length of the Blog model
	def test_description_max_length(self):
		blog = Blog.objects.get(id = 1)
		max_length = blog._meta.get_field('description').max_length
		self.assertEquals(max_length, 2000)

	# Testing the date label of the Blog model
	def test_date_label(self):
		blog = Blog.objects.get(id = 1)
		field_label = blog._meta.get_field('post_date').verbose_name
		self.assertEquals(field_label, 'post date')

	# Testing the date of the Blog model
	def test_date(self):
		blog = Blog.objects.get(id = 1)
		the_date = blog.post_date
		self.assertEquals(the_date, datetime.date.today())

	# Testing the name of the Blog model
	def test_object_name(self):
		blog = Blog.objects.get(id = 1)
		expected_object_name = blog.name
		self.assertEquals(expected_object_name, str(blog))

	# Testing the absolute url of the Blog model
	def test_get_absolute_url(self):
		blog = Blog.objects.get(id = 1)
		self.assertEquals(blog.get_absolute_url(), '/blog/blog/1')

# Blog Author Model tests
class BlogAuthorModelTest(TestCase):
	@classmethod
	# The information all Blog Author model tests are going to use
	def setUpTestData(cls):
		# Test User 1
		test_user1 = User.objects.create_user(username = 'testuser1', password = 'password1')
		test_user1.save()
		# The Blog Author and Blog Author's Bio
		BlogAuthor.objects.create(user = test_user1, bio = "This is test_user1's bio.")

	# Testing the user name label of the Blog Author model
	def test_user_label(self):
		author = BlogAuthor.objects.get(id = 1)
		field_label = author._meta.get_field('user').verbose_name
		self.assertEquals(field_label, 'user')

	# Testing the bio label of the Blog Author model
	def test_bio_label(self):
		author = BlogAuthor.objects.get(id = 1)
		field_label = author._meta.get_field('bio').verbose_name
		self.assertEquals(field_label, 'bio')

	# Testing the bio length of the Blog Author model
	def test_bio_max_length(self):
		author = BlogAuthor.objects.get(id = 1)
		max_length = author._meta.get_field('bio').max_length
		self.assertEquals(max_length, 400)

	# Testing the name of the Blog Author model
	def test_object_name(self):
		author = BlogAuthor.objects.get(id = 1)
		expected_object_name = author.user.username
		self.assertEquals(expected_object_name, str(author))

	# Testing the absolute url of the Blog Author model
	def test_get_absolute_url(self):
		author = BlogAuthor.objects.get(id = 1)
		self.assertEquals(author.get_absolute_url(), '/blog/blogger/1')

# Blog comment tests
class BlogCommentModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		# The information all Blog comment model tests are going to use
		# Test User 1
		test_user1 = User.objects.create_user(username = 'testuser1', password = 'password1')
		test_user1.save()
		# Test User 2
		test_user2 = User.objects.create_user(username = 'testuser2', password = 'password2')
		test_user2.save()
		# The author of the blog post
		blog_author = BlogAuthor.objects.create(user = test_user1, bio = "This is test_user1's bio.")
		# The Test Blog Post
		blog_test = Blog.objects.create(name = 'Test Blog 1', author = blog_author, description = "Test Blog 1 Description")
		# The Test Comment
		blog_comment = BlogComment.objects.create(description = 'Test Blog 1 comment 1 description', author = test_user2, blog = blog_test)

	# Testing the description label of the Blog comment model
	def test_description_label(self):
		blogcomment = BlogComment.objects.get(id = 1)
		field_label = blogcomment._meta.get_field('description').verbose_name
		self.assertEquals(field_label, 'description')

	# Testing the description length of the Blog comment model
	def test_description_max_length(self):
		blogcomment = BlogComment.objects.get(id = 1)
		max_length = blogcomment._meta.get_field('description').max_length
		self.assertEquals(max_length, 1000)

	# Testing the author label of the Blog comment model
	def test_author_label(self):
		blogcomment = BlogComment.objects.get(id = 1)
		field_label = blogcomment._meta.get_field('author').verbose_name
		self.assertEquals(field_label, 'author')

	# Testing the date label of the Blog comment model
	def test_date_label(self):
		blogcomment = BlogComment.objects.get(id = 1)
		field_label = blogcomment._meta.get_field('post_date').verbose_name
		self.assertEquals(field_label, 'post date')

	# Testing the blog label of the Blog comment model
	def test_blog_label(self):
		blogcomment = BlogComment.objects.get(id = 1)
		field_label = blogcomment._meta.get_field('blog').verbose_name
		self.assertEquals(field_label, 'blog')

	# Testing the name of the Blog comment model
	def test_object_name(self):
		blogcomment = BlogComment.objects.get(id = 1)
		expected_object_name = ''
		len_title = 75
		if len(blogcomment.description)>len_title:
			expected_object_name = blogcomment.description[:len_title] + '...'
		else:
			expected_object_name = blogcomment.description
		self.assertEquals(expected_object_name, str(blogcomment))