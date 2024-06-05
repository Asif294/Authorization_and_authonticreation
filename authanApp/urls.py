from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.Signup,name='signup'),
    path('home/',views.home),
    path('profile/',views.profile,name='profile'),
    path('login/',views.Userlogin,name='login'),
    path('logout/',views.Userlogout,name='logout'),
    path('pass_change/',views.pass_change,name='pass_change'),
    path('pass_change2/',views.pass_change2,name='pass_change2'),
]
