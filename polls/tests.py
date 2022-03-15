from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from django.template.loader import render_to_string

from polls.views import index

# Create your tests here.

class PoleDanceTest(TestCase):

    def test_root_url_resolves_to_polls_home_page_view(self):
        found = resolve('/polls/')
        self.assertEqual(found.func, index)

    def test_poll_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request) # this comment should only appear in main
        expected_html = render_to_string('polls/index.html')
        self.assertEqual(response.content.decode(), expected_html) 







