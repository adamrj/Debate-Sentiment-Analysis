from django.db import models

class Tweet(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField()
    query_string = models.CharField(max_length=200)
    candidate = models.CharField(max_length=200)
    score = models.DecimalField(max_digits=6, decimal_places=5, default=0.5)

class Word(models.Model):
	word = models.CharField(max_length=150,db_index=True)
	positive = models.IntegerField()
	negative = models.IntegerField()




