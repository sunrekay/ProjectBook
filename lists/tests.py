from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        responce = self.client.get('')
        self.assertTemplateUsed(responce, 'home.html')

    def test_can_save_a_POST_request(self):
        responce = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', responce.content.decode())
        self.assertTemplateUsed(responce, 'home.html')
