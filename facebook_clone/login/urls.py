from django.urls import path
from .views import RegisterUserView

urlpatterns=[
    path('register/', RegisterUserView.as_view(),name='register') 
]

#we need to bring this path to the project url i.e. facebook_config/urls.py and include it there using include() function