from django.urls import path

from website import views

urlpatterns = [
    path('', views.SettingView.as_view(), name="index"),
]
