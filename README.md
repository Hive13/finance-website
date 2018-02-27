# finance-website
Hive13 Open Finance Website

This is the Open Finance Website located at finance.hive13.org. This was created in order to fulfill the requirement to provide regular financial reports to the membership. The site is build on the Django framework.

Python module requirements: django-queryset-csv

Instructions:
1. Download repo
1. Copy hive13/settings.py.example to hive13/settings.py and edit:
   1. Add the SECRET_KEY or generate a new one.
   1. Add the hostname the websites domain name to ALLOWED_HOSTS
1. Make sure you are in the root of the repo and run `./manage.py runserver`
