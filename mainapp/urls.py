from django.conf.urls import url,include
from . import views
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^accounts/register/',RegistrationView.as_view(success_url='/accounts/login/'),name="register"),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^accounts/login/',LoginView, name="login"),
    url(r'^accounts/logout/',LogoutView.as_view(),name='logout'),
    url(r'^addpost/$',views.addpost,name="addpost"),
    url(r'^profileupdate/(\d)',views.updateprofile,name='updateprofile'),
    url(r'^business/',views.business,name="business"),
    url(r'^facility/(\d)/',views.facility,name='facility'),
    url(r'^search/',views.search,name="serach"),
]

