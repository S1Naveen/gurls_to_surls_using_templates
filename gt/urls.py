from django.urls import path
from gt.views import *

app_name='gt'
urlpatterns=[
    path('hp/',hp,name='hp'),

]
