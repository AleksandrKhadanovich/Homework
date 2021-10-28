'''This module provides extracting news from rss of news portals.
User can choose the quolity of news and output format.'''

import argparse
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys


"""Function for checking connection"""


def connect(url, vrbs=None):
    r = None
    try:
        r = requests.get(url, timeout=10)
        if vrbs:
            print('Connection done well: ', r.status_code)
    except requests.exceptions.RequestException as e:
        print('The connection failed. See exception: ')
        raise SystemExit(e)
        print(e)

    return r


"""Function for extracting info from rss"""


def out_info(r, nlimit):
    try:
        soup = BeautifulSoup(r.content, "xml")
        Feed = soup.find('title').text
        print("\n")
        print(str(Feed))
        if nlimit < 0:
            print("Limit can not be negative")
        else:
            articles = soup.findAll('item', limit=nlimit)
            if not articles:
                print("No articles")
            else:
                return articles
    except Exception as e:
        print(f"Could not parse the xml: {e}")


"""Function for structuring data for json output and standart output"""


def detailed_info(articles, vrbs, js_on):
    descr = ''
    article_list = []
    for a in articles:
        title = a.find('title').text
        link = a.find("link").text
        published = a.find('pubDate').text
        try:     # try to change time format for rss 2.0
            date = datetime.strptime(published, "%Y-%m-%dT%H:%M:%SZ")
            published = datetime.strftime(date, "%H:%M:%S %d.%m.%Y")
        except:
            pass
        try:     # check if description provided
            descr = a.find('description').text
            descr = descr.replace('\n  ', '').replace('\n', '').replace('<br />', '')
        except:
            pass

        if not js_on:     # standart output
            print(50*'-')
            print(title)
            print(link)
            print(published)
            if descr:
                print(descr)
            if not descr and vrbs:
                print('This news has no description')

        if js_on:     # collecting items for json output
            if descr:
                article = {
                    'Title': title,
                    'Link': link,
                    'Published': published,
                    'Description': descr
                    }
            else:
                article = {
                    'Title': title,
                    'Link': link,
                    'Published': published
                    }
            article_list.append(article)
    return article_list


""" Main function + prints info as json in stdout"""


def fromrss(url, nlimit, vrbs=None, js_on=None):
    r = connect(url, vrbs)
    try:
        articles = out_info(r, nlimit)
    except Exception as e:
        print("No articles")
    else:
        d = detailed_info(articles, vrbs, js_on)
        if js_on:
            if vrbs:
                print('Output in json format: ')
            json.dump(d, sys.stdout, indent=3, ensure_ascii=False, separators=(", ", ": "))


'''The argparse module to write user-friendly command-line interfaces.'''


def parse_news():
    parser = argparse.ArgumentParser(description='Pure Python command-line RSS reader.')
    parser.add_argument('source',  type=str,
                        help='RSS URL')
    parser.add_argument('--Limit', default=0, type=int, const=0, nargs='?', metavar='LIMIT',
                        help='Limit news topics if this parameter provided')
    parser.add_argument('--version',  action='version', version='(Final Task)s 1.0',
                        help='Prints version info')
    parser.add_argument('--json',
                        help='Prints result at JSON in stdout', action='store_true')
    parser.add_argument('--verbose',
                        help='Outputs verbose status messages', action="store_true")
    args = parser.parse_args()

    if args.verbose:
        print("Verbose on")
        print('Starting extraction')
        fromrss(args.source, args.Limit, vrbs=args.verbose, js_on=args.json)
        print('Finished extraction')
    else:
        fromrss(args.source, args.Limit, js_on=args.json)


if __name__ == '__main__':
    parse_news()
