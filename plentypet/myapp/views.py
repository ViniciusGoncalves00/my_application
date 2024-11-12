from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Course

def home(request):
    return HttpResponse("Hello, Django!")


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'myapp/course_detail.html', {'course': course})