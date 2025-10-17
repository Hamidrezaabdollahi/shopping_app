from django.urls import path

from .views import HomePageView, AboutUsPage

urlpatterns =[
    path("",HomePageView.as_view(), name="home"),
    path("about/",AboutUsPage.as_view(), name="about"),
]