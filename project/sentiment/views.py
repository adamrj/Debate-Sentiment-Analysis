from django.shortcuts import render, redirect
from django.views.generic import View
from sentiment.models import Tweet, Word
from sentiment.bayes import *
from django.db.models import Avg
from django.http import JsonResponse



class IndexView(View):
    template = 'sentiment/index.html'
    def get(self, request):
        return render(request, self.template)


class BarChartView(View):
	candidate_list = ["Trump", "Bush", "Walker", "Huckabee", "Carson", "Cruz", "Rubio", "Paul", "Christie", "Kasich"]

	def get(self,request):
		candidate_dict = {}
		for candidate in self.candidate_list:
			score = Tweet.objects.filter(candidate = candidate).aggregate(Avg('score'))
			candidate_dict[candidate] = score
		print(candidate_dict)
		return JsonResponse({"candidates":candidate_dict})


class SecondView(View):
    template = 'sentiment/second.html'
  
    def get(self, request):
        return render(request, self.template)



class LineChartView(View):
	candidate_list = ["Trump", "Bush", "Walker", "Huckabee", "Carson", "Cruz", "Rubio", "Paul", "Christie", "Kasich"]

	def get(self,request):
		candidate_dict = {}
		for candidate in self.candidate_list:
			print(candidate)
			tweets = Tweet.objects.filter(candidate = candidate)
			### Create list of all times
			tweet_time_list = {}
			for hours in range(0,4):
				for minutes in range(0,60):
					tweet_time_list[hours*60+minutes] = []
			### Assigns all tweets to a time in the time_list
			for tweet in tweets:
				for time in tweet_time_list:
					if tweet.date.hour * 60 + tweet.date.minute == time:
						tweet_time_list[time].append(tweet)
			## Calculates rolling average
			rolling_average_list = {}
			for x in range(6,4*60):
				score = 0
				length = 0
				for y in range(x-5,x+1):
					tweets = tweet_time_list[y]
					for tweet in tweets:
						length += 1
						score += tweet.score
				if length > 0:
					rolling_average = score / length
					rolling_average_list[x] = rolling_average
			candidate_dict[candidate] = rolling_average_list
		return JsonResponse({"candidates":candidate_dict})
       	


  