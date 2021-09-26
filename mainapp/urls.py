from django.conf.urls import url,include
from . import views
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.views import LoginView
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^accounts/register/',RegistrationView.as_view(),name="register"),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^accounts/login/',LoginView, name="login")
]

