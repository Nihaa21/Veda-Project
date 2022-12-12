
from django.urls import path,include
from .views import User_registration_view



urlpatterns = [
path('register/',User_registration_view.as_view(),name='register'),

]
