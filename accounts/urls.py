from django.urls import path, include

# from product_detail.view import *
from .views import *
from django.views.generic.base import TemplateView 

app_name='accounts'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('wallet/', WalletView.as_view(), name='wallet'),
    path('login/', LoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contact/', ContactView.as_view(), name='contact'),
    #  path('new-entry/', OwnBoardView.as_view(), name='new-entry'),
]
