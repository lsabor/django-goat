from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from django.template.loader import render_to_string

from polls.views import index

# Create your tests here.

# I'm adding a supufluous line here that will just be seen in main
# a second line I guess
class PoleDanceTest(TestCase):

    def test_root_url_resolves_to_polls_home_page_view(self):
        found = resolve('/polls/')
        self.assertEqual(found.func, index)

    def test_poll_home_page_returns_correct_html(self):
        request = HttpRequest() # this change was made in experimental only, let's see what happens
        response = index(request) # this comment should only appear in main
        expected_html = render_to_string('polls/index.html')
        self.assertEqual(response.content.decode(), expected_html) 


# I'm adding some changes to the end of this document
# they're just comments and were made on experimental,
# they are designed not to conflict with recent
# comments made in this same file in main placed well above




