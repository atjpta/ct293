'''
A web crawler for extracting email addresses from web pages.

Takes a string of URLs and requests each page, checks to see if we've
found any emails and prints each email it finds.
'''

import argparse
import re
import sys
import urllib.request

class Crawler(object):

    def __init__(self, urls):
        '''
        @urls: a string containing the (comma separated) URLs to crawl.
        '''
        self.urls = urls.split(',')

    def crawl(self):
        '''
        Iterate the list of URLs and request each page, then parse it and
        print the emails we find.
        '''
        for url in self.urls:
            data = self.request(url)
            #print(data)
            for email in self.process(data):
                print(email)

    @staticmethod
    def request(url):
        '''
        Request @url and return the page contents.
        '''
        response = urllib.request.urlopen(url)
        return response.read().decode("utf-8", "ignore")

    @staticmethod
    def process(data):
        '''
        Process @data and yield the emails we find in it.
        '''
        for email in re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', data):
            yield email


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '--urls', dest='urls', required=True,
        help='A comma separated string of emails.')
    parsed_args = argparser.parse_args()
    crawler = Crawler(parsed_args.urls)
    crawler.crawl()

if __name__ == '__main__':
  sys.exit(main())