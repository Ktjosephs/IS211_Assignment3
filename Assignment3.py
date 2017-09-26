#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 3 Assignment."""

import csv
import argparse
import urllib2
import re


def download_data(url):
    """Fetches data."""
    datafile = urllib2.urlopen(url)
    return datafile

def process_csv(csvdata):
    """Processes a URL linked to a .csv file."""
    readfile = csv.reader(csvdata)
    countline = 0
    img = 0

    fox = ['Firefox', 0]
    chrome = ['Google Chrome', 0]
    safari = ['Safari', 0]
    int_ex = ['Internet Explorer', 0]
    for line in readfile:
        countline += 1
        if re.search("firefox", line[2], re.I):
            fox[1] += 1
        elif re.search(r"int_ex", line[2]):
            int_ex[1] += 1
        elif re.search(r"Chrome", line[2]):
            chrome[1] += 1
        elif re.search(r"Safari", line[2]) and not re.search("Chrome", line[2]):
            safari[1] += 1
        if re.search(r"jpe?g|JPE?G|png|PNG|gif|GIF", line[0]):
            img += 1

    percentage_hit = (float(img) / countline) * 100

    browser_count = [chrome, int_ex, safari, fox]

    top_browser = 0
    top_name = ' '
    for top in browser_count:
        if top[1] > top_browser:
            top_browsr = top[1]
            top_name = top[0]
        else:
            continue

    ans = ('Number of hits = {} Hit percentage = {} Top Browser = \n{}'
           .format(countline, percentage_hit, top_browsr, top_name))
    print ans

def main():
    """Combines downloadData function and processData."""
    if not args.url:
        raise SystemExit
    try:
        data = download_data(args.url)
    except urllib2.URLError:
        print 'Enter only valid URL.'
        raise
    else:
        process_csv(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Assignment3 download weblog.')

    parser.add_argument('--url', action="store", dest="weburl")

    args = parser.parse_args()

    print "This is what I read:"
    csvdata = download_data(args.weburl)
    process_csv(csvdata)

