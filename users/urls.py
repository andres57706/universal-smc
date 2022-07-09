from django.urls import path

from .views import accounts

app_name = 'users'
urlpatterns = [
    path('signup/', accounts.signup, name='signup'),
    path(r'^signin/$', accounts.SigninViewClass.as_view(), name='signin'),
    path(r'^signin/(?P<next>\w+)$', accounts.SigninViewClass.as_view(), name='signin'),
    path('signout/', accounts.SignoutViewClass.as_view(), name='signout'),
]
