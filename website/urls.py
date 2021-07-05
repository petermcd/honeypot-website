from django.urls import path

from website import views

app_name = 'network'
urlpatterns = [
    path('', views.SettingView.as_view(), name="index"),
]
