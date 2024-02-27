from django.urls import path
from comments import views

app_name = 'comments'

urlpatterns = [
    path('comments/', views.CommentList.as_view(), name='index'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name="show"),
]