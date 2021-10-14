from django.shortcuts import render
from django.views import View
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import json
import requests

# @method_decorator(csrf_exempt, name='dispatch')
class HomeView(View):
    #get The sudoku board in Render.
    
    def get(self, request):
        template ='home.html'
        print(request.user)
        try:
            token= request.user.binance_profile_token
            api = 'https://pool.binance.com/mining-api/v1/public/pool/stat?observerToken={}'.format(token)
            # print(api)
            statresponse = requests.get(api).json()
            # print(statresponse)
            # print(statresponse['data']['profitToday']['ETH'])
            user = request.user
            user.profit_today = statresponse['data']['profitToday']['ETH']
            user.profit_yesterday = statresponse['data']['profitYesterday']['ETH']
            api = 'https://pool.binance.com/mining-api/v1/public/pool/profit/miner?observerToken={}'.format(token)
            afterfees = 0.00339751
            minerresponse = requests.get(api).json()
            # print(minerresponse)
            total_amount = afterfees + minerresponse['data']['totalAmount']['ETH']   
            user.amountmined = total_amount
            user.amountachievedafterded = 0.95*total_amount
            user.save()
        except Exception as e:
            print('Error',e)
        return TemplateResponse(request,template)
    
    
    def post(self, request):
        print(request.body)
        # data = json.loads (request.body)
        # solved_board = start(data)
        return  HttpResponse(None, content_type="application/json")