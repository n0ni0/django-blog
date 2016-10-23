from django.test import TestCase
from django.urls import reverse


class ViewTest(TestCase):
    def test_load_home_page(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    def test_load_single_post_view(self):
        response = self.client.get('/hello-world/post/')
        self.assertEquals(response.status_code, 200)

    def test_load_posts_with_same_category(self):
        response = self.client.get('/django/category/')
        self.assertContains(response, '<h1>Posts sobre django</h1>')