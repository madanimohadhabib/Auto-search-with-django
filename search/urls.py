from django.urls import path
from .views import *


urlpatterns = [
    path('',index),
    path('get-names/',get_names)

]
