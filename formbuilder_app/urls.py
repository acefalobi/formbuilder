from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.landing_page, name='landing_page'),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),

    # Form Management
    url(r'^forms/(\d+)/$', views.form_view, name="form-view"),
    url(r'^forms/new/', views.form_new, name="form-new"),
    url(r'^forms/edit/(\d+)/$', views.form_edit, name="form-edit"),
    url(r'^forms/delete/(\d+)/$', views.form_delete, name="form-delete"),
    url(r'^forms/submit/success', views.form_submit_success, name="form-submit-success"),
    url(r'^forms/submissions/(\d+)/$', views.form_submissions, name="form-submissions"),
    url(r'^forms/submissions/download/(\d+)/$', views.form_download_submissions, name="form-download-submissions"),

    # Session Management
    url(r'^accounts/login/', views.login_redirection_page, name="login_redirection_page"),
    url(r'^register/$', views.register_page, name="register_page"),
    url(r'^register/success/$', TemplateView.as_view(template_name="registration/register_success.html")),
    url(r'^logout/', views.logout_page, name="logout_page"),
]
