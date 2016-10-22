from django.test import TestCase

from app.models import Post


class PostMethodTest(TestCase):
    def test_home_contains_posts(self):
        posts = Post.objects.all()
        self.assertGreater(posts, 2)