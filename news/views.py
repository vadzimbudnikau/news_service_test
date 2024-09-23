import logging
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from news.models import News
from news.serializers import NewsSerializer

logger = logging.getLogger(__name__)

class NewsCreateView(APIView):
    """
    API view to create a new News object.
    """

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f'News created: {serializer.data}')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(f'Failed to create news: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsDetailView(APIView):
    """
    API view to retrieve a News object by its ID.
    """

    def get(self, request, pk):
        news = cache.get(f'news_{pk}')
        if not news:
            try:
                news = News.objects.get(pk=pk)
                serializer = NewsSerializer(news)
                cache.set(f'news_{pk}', serializer.data, timeout=60*15)
                logger.debug(f'News retrieved from DB: {serializer.data}')
                return Response(serializer.data)
            except News.DoesNotExist:
                logger.warning(f'News with ID {pk} not found.')
                return Response(status=status.HTTP_404_NOT_FOUND)
        logger.debug(f'News retrieved from cache: {news}')
        return Response(news)
