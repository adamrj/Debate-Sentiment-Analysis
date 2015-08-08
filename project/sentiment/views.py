from django.shortcuts import render, redirect
from django.views.generic import View
from sentiment.secret import *


twitter = Twython(APP_KEY, APP_SECRET)

auth = twitter.get_authentication_tokens()

auth_url = auth['auth_url']



class IndexView(View):
    template = 'sentiment/index.html'
  

    def get(self, request):
        twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        twitter.update_status(status='testing the status')
        return render(request, self.template)