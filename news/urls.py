from django.urls import path
from news.views import NewsCreateView, NewsDetailView

urlpatterns = [
    path('create/', NewsCreateView.as_view(), name='news-create'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
]