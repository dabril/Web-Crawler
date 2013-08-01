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
import urllib2
#import urlparse
from urlparse import urlparse
import getopt
from collections import deque

class Crawler:
    """ Class Crawler """

    def __init__(self, seed):
        """ Crawler Constructor """
        self.o_seeds = [] #original seeds / Domains
        self.rules = [] 
        self.add_seeds(seed)
        self.set_rules()
        self.set_rules()
        self.frontier = deque(self.o_seeds)
        self.visited = []

    def add_seeds(self, seed):
        """ Add starting web domains """
        #TODO seed/s are web URLs
        if type(seed) == list:
            self.o_seeds = seed
        elif type(seed) == str:
            self.o_seeds = [seed]
        else:
            print "Incorrect type of URL seed"
            sys.exit()

    def set_rules(self):
        """ Define rule domains """
        for seed in self.o_seeds:
            domain = str(urlparse(seed).hostname) + str(urlparse(seed).path)
            self.rules.append('^(http://.('+domain+')(.+)$')

    def start(self):
        """ Start Crawling """
        
        fetched_url = 0
        folder_url = str(urlparse(self.o_seeds[0]).hostname)
        if not os.path.exists(folder_url):
            os.mkdir(folder_url)
        while fetched_url < 10 and self.frontier:
            #Fetch URL
            url = self.frontier.popleft()
            print "Fetching " + url + " ..."
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            the_page = response.read()
            print the_page

            fetched_url += 1
            





def main(argv):
    seedurl = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["help", "iseedurl="])
    except getopt.GetoptError:
        print 'Incorrect parameters: crawler.py -i <input see durl>'
        sys.exit(2)
    if opts == [] and args == []:
        print 'Error: Ask help crawler.py -h'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print 'crawler.py -i <input seed url>'
            sys.exit(2)
        elif opt in ("-i", "--iseedurl"):
            seedurl = arg
    print 'The domain to crawl is ', seedurl


    crawler = Crawler(seedurl)
    crawler.start()

if __name__ == "__main__":
    main(sys.argv[1:])



#Below is code to fetch seed URL


    
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



