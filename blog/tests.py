from django.test import TestCase
from .models import Post
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username='testuser',
            email='tushar@gmail.com',
            password='secret'
        )
        self.post=Post.objects.create(
            title='a good title',
            body='nice body content',
            author=self.user,
        )

    def test_string_representation(self):
        post=Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','a good title')
        self.assertEqual(f'{self.post.body}','nice body content')
        self.assertEqual(f'{self.post.author}','testuser')

    def test_post_list_view(self):
        response=self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'nice body')
        self.assertTemplateUsed(response,'home.html')

    def test_post_detail_view(self):
        response=self.client.get('/post/1/')
        no_response=self.client.get('/post/1000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response,'a good title')
        self.assertTemplateUsed(response,'detail.html')
