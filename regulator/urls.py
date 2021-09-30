from django.urls import path, include

# from product_detail.view import *
from .views import *
# from django.views.generic.base import TemplateView 

app_name='regulator'

urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('call-to-mom/', AccountUpdateView.as_view(), name='update')
    #  path('new-entry/', OwnBoardView.as_view(), name='new-entry'),
    
]
