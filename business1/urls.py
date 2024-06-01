from django.urls import path
from .import views


urlpatterns = [
    path('business1/', views.index, name='business1-index'),
    path('post_detail/<int:pk>/', views.post_detail, name='business1-post-detail'),
    path('post_edit/<int:pk>/', views.post_edit, name='business1-post-edit'),
    path('post_delete/<int:pk>/', views.post_delete, name='business1-post-delete'),
]