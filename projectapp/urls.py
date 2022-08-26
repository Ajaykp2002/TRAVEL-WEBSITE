from . import views
from django.urls import path



urlpatterns = [

    path('',views.add,name="add"),



    #path('add/', views.Addition, name="Addition")
    #path('contact/', views.contact, name="contact"),
    #path('details/', views.details, name="details"),
    #path('thank/', views.thank, name="thank")

]