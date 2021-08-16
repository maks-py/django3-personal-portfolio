from django.db import models

class Blog(models.Model):
  title = models.CharField(max_length=200)
  date = models.DateTimeField(auto_now=True)
  description = models.TextField()
  url = models.URLField()

  def __str__(self):
    return self.title