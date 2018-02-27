#!/usr/bin/python

import django
from django.core.cache import cache
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'hive13.settings'
django.setup() # Needed to make django ready from the external script
cache.clear() # Flush all the old cache entry.
