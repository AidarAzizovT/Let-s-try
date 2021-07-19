from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Article(models.Model):
    article_title = models.CharField("Name of article", max_length=100)
    article_text = models.TextField("Text of article")
    pub_date = models.DateTimeField("Published day")
    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return timezone.now() - self.pub_date <=datetime.timedelta(days=7)
class Comment(models.Model):
    comment_author = models.CharField("Author of comment", max_length=50)
    comment_text = models.CharField("Text of comment", max_length=200)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)