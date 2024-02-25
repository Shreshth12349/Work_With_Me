from django.urls import path
from . import views
urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('home', views.home, name='home-page'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('post_project/', views.post_project, name='post_project'),
]