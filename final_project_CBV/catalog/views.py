from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course, Author


def index(request):
    template = 'index.html'
    return render(request, template)


def info(request):
    template = 'info.html'
    return render(request, template)


def not_found(request, exception):
    template = 'not_found.html'
    return render(request, template, status=404)


class CourseListView(ListView):
    model = Course
    ordering = 'id'
    paginate_by = 10


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
    context_object_name = 'course'


class AuthorListView(ListView):
    model = Author
    ordering = 'id'
    paginate_by = 10


class AuthorDetailView(DetailView):
    model = Course
    template_name = 'author_detail.html'
    context_object_name = 'author'
