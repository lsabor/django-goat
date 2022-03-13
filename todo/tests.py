from django.test import TestCase
from django.urls import resolve

from todo.views import index

# Create your tests here.

class SmokeTest(TestCase):

    def test_root_url_resolves_to_todo_home_page_view(self):
        found = resolve('/todo/')
        self.assertEqual(found.func, index)