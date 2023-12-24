from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cats/<int:catid>/', views.category, name='cats'),
    path('post/new/', views.post_info, name='post_new'),
    path('drafts/', views.post_draft, name='post_draft'),
]