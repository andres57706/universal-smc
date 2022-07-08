from django.urls import path

import views

app_name = 'searches'
urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.search, name='get_results'),
    path('create/', views.create, name='create')
]
