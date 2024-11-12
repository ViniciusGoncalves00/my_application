from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Course


def home(request):
    return HttpResponse("Hello, Django!")


def course_detail(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
        return render(
            request,
            "courses/course_detail.html",
            {
                "course": {
                    "title": course.title,
                    "description": course.description,
                    "created_at": str(course.created_at),
                    "pk": course.pk,
                }
            },
        )
    except:
        return HttpResponseRedirect("/")
