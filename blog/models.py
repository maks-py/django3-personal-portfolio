from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
