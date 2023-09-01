from django.test import TestCase, Client
from django.test.client import RequestFactory
from django.urls import reverse
from blog.models import Articulo, Comentario, Noticia
from django.contrib.auth.models import User
import json


class TestViews(TestCase):

  def setUp(self) -> None:
    self.factory = RequestFactory()
    self.client = Client()
    self.user = User.objects.create_user(
      username = 'test1',
      email = 'abc1@gmail.com',
      first_name = 'test',
      last_name = 'unit',
      password = 'Password1990'
    )
    self.client.login(username='test1', password='Password1990')
    self.index_url = reverse('index')
    self.view_url = reverse('Artículos')

  def test_index_GET(self):
    response = self.client.get(self.index_url)

    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'index.html')

  def test_article_view_registered_user_GET(self):
    response = self.client.get(self.view_url)

    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'articles.html')