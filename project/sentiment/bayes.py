import csv
import nltk
from sentiment.models import Word, Tweet

alphabet="abcdefghijklmnopqrstuvxwyz "

def string_tokenizer(string):
	lower_string = string.lower()
	new_string = ''
	for letter in lower_string:
		if letter in alphabet:
			new_string += letter
	word_array = nltk.word_tokenize(new_string)
	return word_array

#training model
def training_model():
	sentiment_dictionary = {}
	#opening dataset
	f = open("/Users/ecatkins/Dropbox/Coding/byte_academy/week-7/Debate-Sentiment-Analysis/project/sentiment/sentiment_dataset.csv","rt")
	reader = csv.reader(f)
	count = 0
	positive_counter = 0
	negative_counter = 0
	for row in reader:
		print (count)
		count += 1
		sentiment = row[1]
		if sentiment == '1':
			positive_counter += 1
		else:
			negative_counter += 1
		word_list = string_tokenizer(row[3])
		### Adds to the sentiment dictionary
		for word in word_list:
			if word == ' ' or word == '':
				pass
			elif word in sentiment_dictionary:
				if sentiment == '1':
					sentiment_dictionary[word][0] += 1
				else:
					sentiment_dictionary[word][1] += 1
			else:
				if sentiment == '1':
					sentiment_dictionary[word] = [1,0]
				else:
					sentiment_dictionary[word] = [0,1]
	# return sentiment_dictionary
	return positive_counter, negative_counter


def bayes_analysis(tweet,positive_tweets,negative_tweets):
	
	#puts string in readable-array
	final_word_list = string_tokenizer(tweet)
	#calculates probability of positive
	prob_pos = positive_tweets / (positive_tweets + negative_tweets)
	for word in final_word_list:
		sentiment_word = Word.objects.filter(word=word)
		if len(sentiment_word) == 1:
			if sentiment_word[0].positive == 0:
				sentiment_word[0].positive = 1
			if sentiment_word[0].negative == 0:
				sentiment_word[0].negative = 1 

			probability_in_positive = sentiment_word[0].positive / positive_tweets
			probability_in_negative = sentiment_word[0].negative / negative_tweets
			prob_pos = probability_in_positive * prob_pos / (probability_in_positive * prob_pos + probability_in_negative * (1-prob_pos))
	
	return prob_pos






	









