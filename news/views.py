from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from news.models import News
from news.serializers import NewsSerializer


class NewsCreateView(APIView):
    """
    API view to create a new News object.

    This view handles POST requests to create a new News entry.
    It uses the NewsSerializer to validate and save the data.
    """

    def post(self, request, *args, **kwargs):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsDetailView(APIView):
    """
    API view to retrieve a News object by its ID.

    This view handles GET requests to retrieve a specific News entry based on its primary key (ID).
    The view returns the data in a JSON format using the NewsSerializer.
    """

    def get(self, request, *args, **kwargs):
        try:
            news = News.objects.get(pk=pk)
            serializer = NewsSerializer(news)
            return Response(serializer.data)
        except News.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
