from django.db import models

class Tweet(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField()
    query_string = models.CharField(max_length=200)
    candidate = models.CharField(max_length=200)



