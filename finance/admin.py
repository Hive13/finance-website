from django.contrib import admin

# Register your models here.
from .models import MonthlyData

class MonthlyDataAdmin(admin.ModelAdmin):
    list_display = ('month', 'year')
    list_filter = ('year','month')
    fieldsets = [
        (None,              {'fields': [('month','year')]}),
        ('Membership',      {'fields': ['members_cornerstone','members_full','members_fullwarden','members_student','members_studentwarden']}),
        ('PNC Main Account',    {'fields': ['pnc_main_beginning','pnc_main_deposits','pnc_main_deductions','pnc_main_ending']}),
        ('PNC Outreach Account',    {'fields': ['pnc_outreach_beginning','pnc_outreach_deposits','pnc_outreach_deductions','pnc_outreach_ending']}),
        ('Paypal Account',  {'fields': ['pp_beginning','pp_credits','pp_payments','pp_fees','pp_transfers','pp_ending']}),
        ('Incomes',   {'fields': ['otherincome','laserincome','otherexpense']}),
        ('Fixed Expenses',  {'fields': ['rent','cable','insurance'], 'classes': ['collapse']}),
    ]

admin.site.register(MonthlyData, MonthlyDataAdmin)
