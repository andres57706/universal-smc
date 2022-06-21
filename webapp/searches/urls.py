from django.urls import path, include

from searches import views

app_name = 'searches'
urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.search, name='get_results'),
]
