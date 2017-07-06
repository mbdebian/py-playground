from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
import re

from lists.views import home_page


# Helpers
def remove_csrf(html_code):
    """ In this version of Django we can't predict the csrf_token, so we need to
    remove it from the response """
    csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
    return re.sub(csrf_regex, '', html_code)


# Create your tests here.

class HomePageTet(TestCase):
    def test_home_page_is_about_todo_lists(self):
        request = HttpRequest()
        response = home_page(request)
        expected_content = render_to_string('home.html', request=request)
        print("=" * 20 + " EXPECTED " + "=" * 20)
        print(remove_csrf(expected_content))
        print("=" * 20 + " RESPONSE " + "=" * 20)
        print(remove_csrf(response.content.decode()))
        self.assertEqual(remove_csrf(response.content.decode()), remove_csrf(expected_content))
        # print("This test fails due to a change in Django API that I still have to figure out")

        # def test_home_page_can_remember_post_request(self):
        # request = HttpRequest()
        # request.method = 'POST'
        # request.POST['item_text'] = 'A new item'
        # response = home_page(request)
        # self.assertIn('A new item', response.content.decode())

from lists.models import Item

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items_to_the_database(self):
        pass
