from rest_framework import generics

from .models import QustionsTest
from .serializers import QustionsTestSerializer

# Create your views here.
class QuestionsList(generics.ListAPIView):
  queryset = QustionsTest.objects.all()
  serializer_class = QustionsTestSerializer

class QuestionDetail(generics.RetrieveAPIView):
  queryset = QustionsTest.objects.all()
  serializer_class = QustionsTestSerializer