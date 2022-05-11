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
    """
    Return Account Data by fetching binance watcher link stored inside db by Admin

    """

    def get(self, request):
        template ='home.html'
        api_string = 'https://pool.binance.com/mining-api/v1/public/pool/'
        api_stat = 'stat?observerToken={}'
        api_miner = 'profit/miner?observerToken={}'
        try:
            token= request.user.binance_profile_token
            
            statresponse = requests.get(api_string+api_stat.format(token)).json()
            print(json.dumps(statresponse,  indent=4))
            user = request.user
            user.profit_today = statresponse['data']['profitToday']['ETH']
            user.profit_yesterday = statresponse['data']['profitYesterday']['ETH']
            afterfees = 0
            if request.user.id == 2:
                afterfees = 0.00339751
            minerresponse = requests.get(api_string+api_miner.format(token)).json()
            print(json.dumps(minerresponse,  indent=4))
            
            minespeed = int(statresponse['data']['hashRate'])
            user.minespeed = minespeed/1000000
            user.amountmined  = afterfees + minerresponse['data']['totalAmount']['ETH']   
            user.amountachievedafterded = 0.95*user.amountmined
            user.save()
        except Exception as e:
            print('Error',e)
            raise
        return TemplateResponse(request,template)
    
    
    def post(self, request):
        
        # data = json.loads (request.body)
        # solved_board = start(data)
        return  HttpResponse(None, content_type="application/json")