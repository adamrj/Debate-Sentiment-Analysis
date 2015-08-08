from django.shortcuts import render, redirect
from django.views.generic import View
from sentiment.models import Tweet, Word
from sentiment.bayes import *
from django.db.models import Avg
from django.http import JsonResponse



class IndexView(View):
    template = 'sentiment/index.html'
    candidate_list = ["Trump", "Bush", "Walker", "Huckabee", "Carson", "Cruz", "Rubio", "Paul", "Christie", "Kasich"]
  
    def get(self, request):
        candidate_dict = {}
        for candidate in self.candidate_list:
        	score = Tweet.objects.filter(candidate = candidate).aggregate(Avg('score'))
        	candidate_dict[candidate] = score
        print(candidate_dict)

        return render(request, self.template)