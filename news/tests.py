from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from news.models import News


class NewsAPITests(APITestCase):

    def setUp(self):
        self.create_url = reverse('news-create')
        self.news_detail_url = lambda id: reverse('news-detail', args=[id])

    def test_create_news(self):
        data = {
            'title': 'Test News',
            'content': 'This is a test news content.'
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(News.objects.count(), 1)
        self.assertEqual(News.objects.get().title, 'Test News')

    def test_get_news(self):
        news = News.objects.create(title='Test News', content='This is a test news content.')
        response = self.client.get(self.news_detail_url(news.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], news.title)

    def test_get_nonexistent_news(self):
        response = self.client.get(self.news_detail_url(999))  # ID that does not exist
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_news(self):
        news = News.objects.create(title='Test News', content='This is a test news content.')
        update_data = {
            'title': 'Updated Test News',
            'content': 'This is updated content.'
        }
        response = self.client.put(self.news_detail_url(news.id), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(News.objects.get(id=news.id).title, 'Updated Test News')

    def test_delete_news(self):
        news = News.objects.create(title='Test News', content='This is a test news content.')
        response = self.client.delete(self.news_detail_url(news.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(News.objects.count(), 0)
