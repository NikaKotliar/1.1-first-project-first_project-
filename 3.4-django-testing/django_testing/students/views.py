from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from students.filters import CourseFilter
from students.models import Course
from students.serializers import CourseSerializer


class CoursesViewSet(ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filterset_class = CourseFilter
    filter_backends = [DjangoFilterBackend, SearchFilter ]
    search_fields = ['id', 'name']

