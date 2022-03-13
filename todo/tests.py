from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from todo.views import index

# Create your tests here.

class SmokeTest(TestCase):

    def test_root_url_resolves_to_todo_home_page_view(self):
        found = resolve('/todo/')
        self.assertEqual(found.func, index)

    def test_todo_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>',response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))