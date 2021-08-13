from django.urls import path, include
from .views import VerifyCardViewset, home


urlpatterns = [
    path('', home, name="home"),
    path('api/v1/verify_card', VerifyCardViewset.as_view(), name='message')
]
