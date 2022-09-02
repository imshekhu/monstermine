from django.shortcuts import render
from django.views import View
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import json
import requests
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
# from .models import 

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
            # print(json.dumps(statresponse,  indent=4))
            user = request.user
            user.profit_today = statresponse['data']['profitToday']['ETH']
            user.profit_yesterday = statresponse['data']['profitYesterday']['ETH']
            afterfees = 0
            if request.user.id == 2:
                afterfees = 0.00339751
            minerresponse = requests.get(api_string+api_miner.format(token)).json()
            # print(json.dumps(minerresponse,  indent=4))
            
            minespeed = int(statresponse['data']['hashRate'])
            user.minespeed = minespeed/1000000
            user.amountmined  = afterfees + minerresponse['data']['totalAmount']['ETH']   
            user.amountachievedafterded = 0.95*user.amountmined
            
            user.in_wallet_amount = float(user.amountachievedafterded) - (float(user.withdrawn_amount) + float(user.in_staking))
            user.save()
        except Exception as e:
            print('Error',e)
            # raise
            # raise
        return TemplateResponse(request,template)
    
    
    def post(self, request):
        
        # data = json.loads (request.body)
        # solved_board = start(data)
        return  HttpResponse(None, content_type="application/json")
    
class WalletView(View):
        """
        Return Account Data by fetching binance watcher link stored inside db by Admin

        """

        def get(self, request):
            template ='wallet.html'
            
            return TemplateResponse(request, template)
            
@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
        """
        Return Account Data by fetching binance watcher link stored inside db by Admin

        """

        def post(self, request):
            
            try :
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    response={'status': 1, 'message': "Ok"}
                    return HttpResponse(json.dumps(response), content_type='application/json')
                
                response = {'status':0, 'message': "Username Password Incorrect"}
                return HttpResponse(json.dumps(response), content_type='application/json')
            except Exception as e:
                print("Error in Login view", str(e))
                response = {'status':0, 'message': "Error!! Please try again after sometime"}
                return HttpResponse(json.dumps(response), content_type='application/json')
                
class ContactView(View):
    """_summary_

    Args:
        View (_type_): Contact page view 
    """
    
    def get(self, request):
            template ='contact.html'
            
            return TemplateResponse(request, template)    
    
            # if request.method == "POST":
            #     current_user_profile = request.user.profile
            #     data = request.POST
            #     action = data.get("follow")
            # if action == "follow":
            #     current_user_profile.follows.add(profile)
            # elif action == "unfollow":
            #     current_user_profile.follows.remove(profile)
            #     current_user_profile.save()
        