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
		return JsonResponse({"candidates":candidate_dict})


class SecondView(View):
    template = 'sentiment/second.html'
    candidate_list = ["Trump", "Bush", "Walker", "Huckabee", "Carson", "Cruz", "Rubio", "Paul", "Christie", "Kasich"]

    def get(self, request):
        return render(request, self.template, {'candidates': self.candidate_list})



class LineChartView(View):
	candidate_list = ["Trump", "Bush", "Walker", "Huckabee", "Carson", "Cruz", "Rubio", "Paul", "Christie", "Kasich"]

	def get(self,request):
		candidate_dict = {}
		for candidate in self.candidate_list:
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
       	
class TweetView(View):

	def get(self, request):
		print('in tweet')
		time = int(float(request.GET.get('time')))
		candidate = request.GET.get('candidate')
		rating = float(request.GET.get('rating'))
		# print(time)
		tweets = Tweet.objects.filter(candidate=candidate)
		# print(tweets.count())
		# print(tweets[0].date)
		# print(tweets[0].date.hour)
		# print(tweets[0].date.minute)
		for tweet in tweets:
			print(time)
			print(tweet.date.hour * 60 + tweet.date.minute)
			if tweet.date.hour * 60 + tweet.date.minute in range(time-5,time+5) and rating -0.05 < tweet.score < rating + 0.05 :
				return JsonResponse({"tweet": tweet.text, "score": tweet.score, "date": tweet.date})
		return JsonResponse({"tweet": "No Tweet found"})


class ThirdView(View):
    template = 'sentiment/third.html'
    candidate_list = ["Trump", "Bush", "Walker", "Huckabee", "Carson", "Cruz", "Rubio", "Paul", "Christie", "Kasich"]

    def get(self, request):
        return render(request, self.template, {'candidates': self.candidate_list})


class DotChartView(View):

	def get(self,request):
		all_tweets = Tweet.objects.all()
		list_tweets = []
		for tweet in all_tweets:
			time = tweet.date.hour * 60 + tweet.date.minute 
			list_tweets.append({"text":tweet.text, "time":time,"score":tweet.score,"candidate":tweet.candidate})

		return JsonResponse({"all_tweets":list_tweets})

  