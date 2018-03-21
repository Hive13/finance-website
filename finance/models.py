from __future__ import unicode_literals

import datetime
from calendar import monthrange
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

MONTHS = (
    (1,"January"),
    (2,"February"),
    (3,"March"),
    (4,"April"),
    (5,"May"),
    (6,"June"),
    (7,"July"),
    (8,"August"),
    (9,"September"),
    (10,"October"),
    (11,"November"),
    (12,"December"),
)

def tuplify(x): return (x,str(x))   # str(x) if needed

def DefaultMonth():
    if timezone.now().month == 1:
        return 12
    else:
        return timezone.now().month - 1

def DefaultYear():
    if timezone.now().month == 1:
        return timezone.now().year - 1
    else:
        return timezone.now().year

def YearRange():
    current_year = timezone.now().year
    YEARS = map(tuplify, range(2009, current_year + 2))
    return YEARS

class MonthlyData(models.Model):
    #Date
    year = models.IntegerField(default=DefaultYear,choices=YearRange())
    month = models.IntegerField(default=DefaultMonth,choices=MONTHS)
    #Membership info
    members_cornerstone = models.IntegerField(default=0)
    members_full = models.IntegerField(default=0)
    members_fullwarden = models.IntegerField(default=0)
    members_student = models.IntegerField(default=0)
    members_studentwarden = models.IntegerField(default=0)
    #Balance: PNC
    pnc_main_beginning = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    pnc_main_deposits = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    pnc_main_deductions = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    pnc_main_ending = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    #Balance: PNC Outreach
    pnc_outreach_beginning = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    pnc_outreach_deposits = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    pnc_outreach_deductions = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    pnc_outreach_ending = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    #Balance: Paypal
    pp_beginning = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    pp_credits = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    pp_fees = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    pp_payments = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    pp_transfers = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    pp_ending = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    #Income
    otherincome = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    laserincome = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    #Expenses
    otherexpense = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    rent = models.DecimalField(max_digits=9, decimal_places=2, default=1150.00)
    cable = models.DecimalField(max_digits=9, decimal_places=2, default=64.15)
    insurance = models.DecimalField(max_digits=9, decimal_places=2, default=59.51)
    ###Dynamic Properties
    #Last day of the month
    @property
    def enddate(self):
        day = monthrange(self.year,self.month)[1]
        return datetime.date(self.year, self.month, day)
    #Last day of the month, javascript format
    @property
    def jsdate(self):
        day = monthrange(self.year,self.month)[1]
        return [self.year, self.month, day]
    #Readable month name
    @property
    def monthname(self):
	for mon in MONTHS:
		if mon[0] == self.month:
			mname=mon[1]
        return mname
    #Combined balances
    @property
    def combinedbeginning(self):
        return self.pnc_main_beginning + self.pnc_outreach_beginning + self.pp_beginning
    @property
    def combinedending(self):
        return self.pnc_main_ending + self.pnc_outreach_ending + self.pp_ending
    #In-out value
    @property
    def inout(self):
        return self.combinedending - self.combinedbeginning
    #Total membership
    @property
    def members_total(self):
        return self.members_cornerstone + self.members_full + self.members_fullwarden + self.members_student + self.members_studentwarden
    #Income values based on membership numbers
    @property
    def memberincome_cornerstone(self):
        return self.members_cornerstone * 100
    @property
    def memberincome_full(self):
        return self.members_full * 50
    @property
    def memberincome_fullwarden(self):
        return self.members_fullwarden * 25
    @property
    def memberincome_student(self):
        return self.members_student * 13.37
    @property
    def memberincome_studentwarden(self):
        return self.members_studentwarden * 1
    #Compatibility for past data without membership numbers
    def has_memberdata(self):
        if self.members_total == 0:
            return False
        else:
            return True
    class Meta:
        get_latest_by = "pk"
