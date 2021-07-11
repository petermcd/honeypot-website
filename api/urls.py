from django.urls import path

from api import views

urlpatterns = [
    path('country/', views.country_view),
    path('country/<str:country>', views.country_view),
    path('country/<str:country>/', views.country_view),
]
