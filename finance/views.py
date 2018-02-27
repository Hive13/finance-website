from django.views import generic
import csv
from django.http import HttpResponse
from .models import MonthlyData
from djqscsv import render_to_csv_response

class IndexView(generic.ListView):
    template_name = 'finance/index.html'
    context_object_name = 'month_list'
    def get_queryset(self):
        return MonthlyData.objects.order_by('year','month')

def ExportView(request, exportCSV):
    qs = MonthlyData.objects.order_by('year','month')
    return render_to_csv_response(qs)
