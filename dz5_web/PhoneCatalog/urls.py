from django.conf.urls import url
from . import views

app_name = 'phone catalog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.phone, name='phone'),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^password-change/', views.PasswordChangeView.as_view()),
]