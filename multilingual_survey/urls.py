from django.conf.urls import url
from multilingual_survey import views


urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', views.survey_form, name='form'),
    url(r'^success/(?P<uuid>\w+)/$', views.survey_success, name='success'),
]
