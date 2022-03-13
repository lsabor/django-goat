from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from django.template.loader import render_to_string

from todo.views import index

# Create your tests here.

class SmokeTest(TestCase):

    def test_root_url_resolves_to_todo_home_page_view(self):
        found = resolve('/todo/')
        self.assertEqual(found.func, index)

    def test_todo_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        expected_html = render_to_string('todo/home_page.html')
        self.assertEqual(response.content.decode(), expected_html)