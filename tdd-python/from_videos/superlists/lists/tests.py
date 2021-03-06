from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
import re

from lists.models import Item
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
        #print("=" * 20 + " EXPECTED " + "=" * 20)
        #print(remove_csrf(expected_content))
        #print("=" * 20 + " RESPONSE " + "=" * 20)
        #print(remove_csrf(response.content.decode()))
        self.assertEqual(remove_csrf(response.content.decode()), remove_csrf(expected_content))
        # print("This test fails due to a change in Django API that I still have to figure out")

        # def test_home_page_can_remember_post_request(self):
        # request = HttpRequest()
        # request.method = 'POST'
        # request.POST['item_text'] = 'A new item'
        # response = home_page(request)
        # self.assertIn('A new item', response.content.decode())

    def test_home_page_shows_items_in_database(self):
        Item.objects.create(text='Item 1')
        Item.objects.create(text='Item 2')

        request = HttpRequest()
        response = home_page(request)

        self.assertIn('Item 1', response.content.decode())
        self.assertIn('Item 2', response.content.decode())

    def test_home_page_can_save_post_request_to_database(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new item'

        response = home_page(request)

        item_from_db = Item.objects.all()[0]
        self.assertEqual(item_from_db.text, 'A new item')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/')


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items_to_the_database(self):
        # Create items and save them to the database
        first_item = Item()
        first_item.text = 'Item the first'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        # Retrieve them from the database
        first_item_from_db = Item.objects.all()[0]
        self.assertEqual(first_item_from_db.text, first_item.text)
        second_item_from_db = Item.objects.all()[1]
        self.assertEqual(second_item_from_db.text, second_item.text)
