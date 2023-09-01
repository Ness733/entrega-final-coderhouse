from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import index, ArticlesView, about, searchResults, ArticleCreateView, ArticleDetails


class TestUrls(SimpleTestCase):

  def test_index_resolves(self):
    url = reverse('index')
    self.assertEquals(resolve(url).func, index)

  def test_articles_resolves(self):
    url = reverse('Artículos')
    self.assertEquals(resolve(url).func.view_class, ArticlesView)

  def test_about_resolves(self):
    url = reverse('Sobre Mi')
    self.assertEquals(resolve(url).func, about)

  def test_results_resolves(self):
    url = reverse('Resultados')
    self.assertEquals(resolve(url).func, searchResults)
  
  def test_create_article_resolves(self):
    url = reverse('Crear Artículo')
    self.assertEquals(resolve(url).func.view_class, ArticleCreateView)
  
  def test_details_article_resolves(self):
    url = reverse('Detalle Artículo', args=['6'])
    self.assertEquals(resolve(url).func.view_class, ArticleDetails)