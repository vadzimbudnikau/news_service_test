from django.urls import path
from news.views import NewsCreateView, NewsDetailView, NewsUpdateView, NewsDeleteView

urlpatterns = [
    path('create/', NewsCreateView.as_view(), name='news-create'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
 path('<int:pk>/update/', NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news-delete'),
]