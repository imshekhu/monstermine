from django.shortcuts import render
from django.views import View
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import json

# @method_decorator(csrf_exempt, name='dispatch')
class HomeView(View):
    #get The sudoku board in Render.
    
    def get(self, request):
        template ='home.html'
        return TemplateResponse(request,template)
    
    
    def post(self, request):
        print(request.body)
        # data = json.loads (request.body)
        # solved_board = start(data)
        return  HttpResponse(None, content_type="application/json")