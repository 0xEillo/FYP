from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import LlangenithListView, CaswellListView, LanglandListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', views.home, name='home'),

    path('llangenith/', LlangenithListView.as_view(), name='llangenith'),
    path('llangenith/<int:pk>/', PostDetailView.as_view(), name='llangenith-post-detail'),
    path('llangenith/new/', PostCreateView.as_view(), name='llangenith-post-create'),
    path('llangenith/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('llangenith/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('caswell/', CaswellListView.as_view(), name='caswell'),
    path('caswell/<int:pk>/', PostDetailView.as_view(), name='caswell-post-detail'),
    path('caswell/new/', PostCreateView.as_view(), name='caswell-post-create'),
    path('caswell/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('caswell/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('langland/', LanglandListView.as_view(), name='langland'),
    path('langland/<int:pk>/', PostDetailView.as_view(), name='langland-post-detail'),
    path('langland/new/', PostCreateView.as_view(), name='langland-post-create'),
    path('langland/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('langland/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)