from django.urls import path
from .import views


urlpatterns = [
    path('api/language', views.LanguageView.as_view()),
    path('api/framework/', views.FrameworkView.as_view())
]