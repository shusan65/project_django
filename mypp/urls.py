from django.urls import path
from.views.mainview import index_page
from.views.authview import register_method,login_method

urlpatterns=[
     path('index/',index_page,name="index"),
     path('login/',login_method,name='login'),
     path('',register_method,name='register')
    ]