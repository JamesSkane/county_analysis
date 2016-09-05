
from django.conf.urls import url

from . import views, charts



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^county/$', views.Food_Desert_list, name='Food_Desert_list'),
    url(r'^chart/$', views.chart, name="simple_chart"),

    #url(r'^chart/$', views.chart_view, name='chart'),
    url(r'^detail/$', views.detail, name='detail'),

]