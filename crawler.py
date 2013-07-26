#!/usr/bin/env python
# -*- coding: utf8 -*-
#==============================================================================
# FILE NAME: crawler.py
# AUTHOR: Daniel Abril
# CREATED: Fri 26 Jul 2013 10:11:32 AM CEST
# PROJECT: ---
#
#== DESCRIPTION: ---
# ---
# NOTES: ---
#==============================================================================

import os
import re
import sys
import urllib
import urlparse

#Below is code to fetch seed URL

f = urllib.urlopen('http://www.iiia.csic.es')

for line in f:
    print str(line)
    import ipdb; ipdb.set_trace() # BREAKPOINT
    
# be polite
# 1 second wait between successive URL fetch request.



def check_domain(url):
    """ check if the url to fetch is on the domaine selected """
