from rest_framework import serializers

from .models import QustionsTest, PSSTest, PSSResult

class QustionsTestSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      "id",
      "content",
      "answer_zero",
      "answer_one",
      "answer_two",
      "answer_three",
      "answer_four",
    )
    model = QustionsTest