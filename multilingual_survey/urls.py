from django.conf.urls import patterns, include, url
from multilingual_survey import views


urlpatterns = patterns('',
    url(r'^(?P<slug>[\w-]+)/$', views.survey_form, name='form'),
    url(r'^success/(?P<uuid>\w+)/$', views.survey_success, name='success'),
)
