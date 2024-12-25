from django.urls import path

from .views import QuestionsList, QuestionDetail

urlpatterns = [
  path("question/<int:pk>/", QuestionDetail.as_view(), name="question_detail"),
  path("questions/", QuestionsList.as_view(), name="questions_list"),
]