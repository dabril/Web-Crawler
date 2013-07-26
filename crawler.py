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
import getopt

def main(argv):
    seedurl = ''
    try:
        opts, args = getopt.getopt(argv,"hi",["help", "iseedurl="])
    except getopt.GetoptError:
        print 'Incorrect parameters: crawler.py -i <input see durl>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print 'crawler.py -i <input seed url>'
            sys.exit()
        elif opt in ("-i", "--iseedurl"):
            seedurl = arg
    print 'Input file is "', seedurl

if __name__ == "__main__":
    main(sys.argv[1:])



#Below is code to fetch seed URL

#f = urllib.urlopen('http://www.iiia.csic.es')

#for line in f:
    #print str(line)
    ##import ipdb; ipdb.set_trace() # BREAKPOINT
    
# be polite
# 1 second wait between successive URL fetch request.


#Initially, the URL frontier contains the seed set; as pages are fetched, the
#corresponding URLs are deleted from the URL frontier

#pick URL from the frontier
#fetch the document at the URL
#parse the URL
#Extract links from it to other docs (URLs)
#for each extracted URL
    #Ensure certain URL filter
    #Check if it is already in the frontier (duplicate URL)


def check_domain(URL, domain):
    """ check if the URL to fetch is on the domain selected """
    parts = URL.split('/')
    #if doamin is in parts
