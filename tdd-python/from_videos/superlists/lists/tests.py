from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from lists.views import home_page

# Create your tests here.

class HomePageTet(TestCase):

    def test_home_page_is_about_todo_lists(self):
        request = HttpRequest()
        response = home_page(request)
        expected_content = render_to_string('home.html', request=request)
        print(expected_content)
        print("=" * 80)
        print(response.content.decode())
        self.assertEqual(response.content.decode(), expected_content)
