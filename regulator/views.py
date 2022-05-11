from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import json
from accounts.models import UserBase

@method_decorator(csrf_exempt, name='dispatch')
class AccountUpdateView(View):
    def post(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        phone = data['phone']
        # print(phone)
        currentcoin = data['currentcoin']
        minespeed = data['minespeed']
        minerconnected = data['minerconnected']
        
        user = self.get_user_by_phone(phone)
        if user:
            user.currentcoin = currentcoin
            user.minespeed = minespeed
            user.minerconnected = minerconnected
            user.save()
            return  HttpResponse(json.dumps({"msg":"call to MoM successfull",  "status":"Success"}), content_type="application/json")
        else:
            return  HttpResponse(json.dumps({"msg":"call to MoM unsuccessfull", "status":"FAIL"}), content_type="application/json")
        # data = json.loads (request.body)
    
    def get_user_by_phone(self, phone):
        try:
            return UserBase.objects.get(phone=phone)
        except UserBase.DoesNotExist:
            return None