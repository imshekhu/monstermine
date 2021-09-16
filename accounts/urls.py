from django.urls import path, include

# from product_detail.view import *
from .views import *
from django.views.generic.base import TemplateView 

app_name='accounts'

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls'))
    #  path('new-entry/', OwnBoardView.as_view(), name='new-entry'),
]
