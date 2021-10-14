from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.CommentsViews.as_view()),
    path('comments/<int:pk>/replies/', views.RepliesViews.as_view()),
    path('likes/<int:pk>/', views.Likes.as_view()),
    path('dislikes/<int:pk>/', views.Dislikes.as_view())
]