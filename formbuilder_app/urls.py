from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
url(r'^$', views.landing_page, name='landing_page'),

# Session Management
url(r'^accounts/login/', views.login_redirection_page, name="login_redirection_page"),
url(r'^register/$', views.register_page, name="register_page"),
url(r'^register/success/$', TemplateView.as_view(template_name="registration/register_success.html")),
url(r'^logout/', views.logout_page, name="logout_page"),
]
