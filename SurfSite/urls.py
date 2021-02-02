from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', views.home, name='home'),
    path('llangenith/', PostListView.as_view(), name='llangenith'),
    path('llangenith/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('llangenith/new/', PostCreateView.as_view(), name='post-create'),
    path('llangenith/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('llangenith/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
]