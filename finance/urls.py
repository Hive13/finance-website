from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views

app_name = 'finance'
urlpatterns = [
    url(r'^$', cache_page(60 * 60)(views.IndexView.as_view()), {'tab':"balance"}, name='index'),
    url(r'^balance', cache_page(60 * 60)(views.IndexView.as_view()), {'tab':"balance"}, name='balance'),
    url(r'^membership', cache_page(60 * 60)(views.IndexView.as_view()), {'tab':"membership"}, name='membership'),
    url(r'^expensesincome', cache_page(60 * 60)(views.IndexView.as_view()), {'tab':"expensesincome"}, name='expensesincome'),
    url(r'^rawdata', cache_page(60 * 60)(views.IndexView.as_view()), {'tab':"rawdata"}, name='rawdata'),
    url(r'^export', cache_page(60 * 60)(views.ExportView), {"exportCSV": True}, name='export'),
]
