from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='create_post'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comments'),
    path('post/<int:pk>/like/', views.toggle_like, name='toggle_like'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('register/', views.register, name='register'),
]
