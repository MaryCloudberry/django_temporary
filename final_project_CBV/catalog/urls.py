from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('courses/', views.CourseListView.as_view(), name='courses'),
    path('course_detail/<int:pk>/', views.CourseDetailView.as_view(),
         name='course_detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author_detail/<int:pk>/', views.AuthorDetailView.as_view(),
         name='author_detail'),
]
