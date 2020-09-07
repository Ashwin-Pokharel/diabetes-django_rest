from django.contrib import admin
from django.urls import path, include  , re_path
from .views import predictDiabetes


urlpatterns = [
    re_path(r'^predict' , predictDiabetes , name="predict")
]