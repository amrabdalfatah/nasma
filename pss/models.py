from django.db import models

# Create your models here.
class PSSTest(models.Model):
  # test_id
  title = models.CharField(max_length=10)
  description = models.CharField(max_length=100)

  def __str__(self):
    return self.title
  
class QustionsTest(models.Model):
  # question_id
  content = models.CharField(max_length=400)
  multichoiceanswer = models.CharField(max_length=100)

  def __str__(self):
    return self.content
  

class PSSResult(models.Model):
  result_id = models.IntegerField()
  score = models.IntegerField()
  test_date = models.DateTimeField(auto_created=True)
  level = models.CharField(max_length=10)
  # user_id, test_id