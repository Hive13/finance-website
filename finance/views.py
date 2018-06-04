from django.views import generic
import csv
from django.http import HttpResponse
from .models import MonthlyData
from djqscsv import render_to_csv_response

class IndexView(generic.ListView):
    template_name = 'finance/index.html'
    context_object_name = 'month_list'
    tab=None
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        if 'tab' in self.kwargs:
            context['tab'] = self.kwargs['tab']
        return context
    def get_queryset(self):
        return MonthlyData.objects.order_by('year','month')

def ExportView(request, exportCSV):
    qs = MonthlyData.objects.order_by('year','month')
    return render_to_csv_response(qs)
