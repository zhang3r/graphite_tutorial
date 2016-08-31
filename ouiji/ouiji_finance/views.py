from django.shortcuts import render
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Quote
from django.http import HttpResponse
from django.http import HttpRequest
import requests
# Create your views here.


api_key = 'b52f7fea9c12806f2b3353ac43a1df6f'
api_url = 'http://marketdata.websol.barchart.com/'



@api_view(['GET',])
def single_quote(request,qn):
	"""
	one single stock quote
	"""

	if request.method == 'GET':
		# print(request.query_params)
		symbol = qn
		r = requests.get(api_url+'getQuote.json?key='+api_key+'&symbols='+symbol)
		# print(r['results'])
		# price = r['results'][0]['lastPrice']
		# date = r['results'][0]['tradeTimestamp']
		print(r.json())
		return HttpResponse(r.json()['results'][0]['lastPrice'])
		# return Request(api_url+'getQuote.json/?key='+api_key+'&symbols='+symbol)

@api_view(['GET',])
def dash_view(request):
	"""
	dashboard view
	contains: Dow, nasdaq, s&p
	"""
	return HttpResponse('dashview')