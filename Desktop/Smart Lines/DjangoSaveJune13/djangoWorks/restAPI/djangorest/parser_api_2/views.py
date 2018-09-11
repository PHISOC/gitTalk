from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import requests
import urllib3
import json
import math
import time
import re
import os
from bs4 import BeautifulSoup
from django.http import HttpResponse




def pinnacleScraper(request):
	url = "http://api.betmonitoring.com/pinnacle/baseball"
	response = requests.get(url)
	print (response.status_code)
	return HttpResponse(response,content_type = 'application/json; charset=utf8')

def bodogScraper(request):
	url = "http://api.betmonitoring.com/bodog/baseball"
	response = requests.get(url)
	print (response.status_code)
	return HttpResponse(response,content_type = 'application/json; charset=utf8')

def sportsInteractionScraper(request):
	url = "http://api.betmonitoring.com/sportsinteraction/baseball"
	response = requests.get(url)
	print (response.status_code)
	return HttpResponse(response,content_type = 'application/json; charset=utf8')

# def bodogScraper(request):
# 	gamesList = {'game':'yield'}
# 	#http://api.betmonitoring.com/bodog/baseball
# 	print(gamesList)
# 	return HttpResponse(json.dumps(gamesList),content_type = 'application/json; charset=utf8')
