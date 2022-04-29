
from rest_framework.viewsets import ModelViewSet

from .models import Student
from .serializers import StudentsSerializer


class StudentsViewSet(ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentsSerializer
