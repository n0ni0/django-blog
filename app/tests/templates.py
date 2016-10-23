from django.test import TestCase


class TemplateTest(TestCase):
    def test_that_home_contains_navbar_with_blog_link(self):
        response = self.client.get("/")
        self.assertContains(response, '<a class="navbar-brand" href="/">Blog</a>')

    def test_that_home_contains_jumbotron(self):
        response = self.client.get("/")
        self.assertContains(response, '<div class="jumbotron">')
