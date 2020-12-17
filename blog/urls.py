from django.urls import path
from . import views
from .views import PostDeleteView

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name="post_list"), # post_list 뷰 함수 연결
    path('post/<int:pk>/', views.post_detail, name='post_detail'), # post/2와 같은 url일 때, 디테일 뷰로 연결
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]