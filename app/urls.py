from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.Login, name='login'),
    path('available/', views.Availability, name='available'),
    path('plant/', views.Plant, name='plant'),
    path('treatment/', views.Treatment, name='treatment'),
    path('aboutUs/', views.AboutUs, name='aboutUs'),
    path('contacUs/', views.ContactUs, name='contactUs'),
    path('logout/', views.logout, name='logout'),
    path('product/', views.Product, name = 'product'),
    path('faqs/', views.FAQS, name = 'faqs'),
    path('privacy/', views.Privacy, name = 'privacy'),
    path('medicine/', views.Medicine, name = 'medicine'),
    path('del_user/<str:pk>/', views.del_user, name = 'del_user'),
    
]