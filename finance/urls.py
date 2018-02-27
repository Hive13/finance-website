from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views

app_name = 'finance'
urlpatterns = [
    url(r'^$', cache_page(60 * 60)(views.IndexView.as_view()), name='index'),
    url(r'^export', cache_page(60 * 60)(views.ExportView), {"exportCSV": True}, name='export'),
    #url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^export', views.ExportView, {"exportCSV": True}, name='export'),
]
