'''This module provides extracting news from rss of news portals.
User can choose the quolity of news and output format as well as sort news by date'''

import argparse
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys
from pathlib import Path
import os


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
    except Exception as e:
        print('The extraction2 failed. See exception: ')
        print(e)
    return r


"""Function for extracting information from rss"""


def out_info(r, nlimit):
    try:
        soup = BeautifulSoup(r.content, "xml")
        Feed = soup.find('title').text
        if nlimit < 0:
            print("Limit can not be negative")
        else:
            articles = soup.findAll('item', limit=nlimit)
            if not articles:
                print("No articles")
            else:
                return articles, str(Feed)
    except Exception as e:
        print('Could not parse the xml: ')
        print(e)


"""Function for converting date"""


def date_convert(date):
    try:     # try to change time format for rss 2.0
        intdate = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
        published = datetime.strftime(intdate, "%d.%m.%Y %H:%M:%S")
    except:
        pass
    try:    # try to change time format for rss 1.0
        intdate = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S %z")
        published = datetime.strftime(intdate, "%d.%m.%Y %H:%M:%S")
    except:
        pass
    try:    # try to change time format for rss 1.0
        intdate = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S %Z")
        published = datetime.strftime(intdate, "%d.%m.%Y %H:%M:%S")
    except:
        pass
    return published


"""Function for structuring data for json output and standart output,
for saving data in standart and json formats"""


def detailed_info(articles, vrbs, js_on, date, feed, enc):
    descr = ''
    media = ''
    article_list = []
    with open(Path(Path.cwd(), 'newslog.txt'), 'a', encoding=enc) as writer:
        writer.write(feed + '\n' + '\n')
    if not date and not js_on:
        print('\n' + feed)

    for a in articles:
        title = a.find('title').text
        link = a.find("link").text
        published = a.find('pubDate').text

        published = date_convert(published)

        try:     # check if description provided
            descr = a.find('description').text
            descr = descr.replace('\n  ', '').replace('\n', '').replace('<br />', '').replace('\n ', '')
        except:
            pass
        try:    # check if media provided
            if a.find('media:content'):
                tag = a.find('media:content')
            else:
                tag = a.find('enclosure')
            media = tag.get('url')
        except:
            pass

        with open(Path(Path.cwd(), 'newslog.txt'), 'a', encoding=enc) as writer:    # saving data to log file
            writer.write ('Title:' + title + '\n' + 'link:' + link + '\n' + 'Published: ' + published + '\n')
            if descr:
                writer.write(f"Description: {descr} \n")
            if media:
                writer.write(f'Media:{media}' + '\n')
            writer.write(50*'-' + '\n')

        if not date and not js_on:     # standart output
            print(50*'-')
            print(title)
            print(link)
            print(published)
            if descr:
                print(descr)
            if media:
                print(f'Media: {media}')
            if not descr and vrbs:
                print('This news has no description')

        if descr and not media:  # collecting items for json output
            article = {
                        'Title': title,
                        'Link': link,
                        'Published': published,
                        'Description': descr
                        }
        if descr and media:
            article = {
                        'Title': title,
                        'Link': link,
                        'Published': published,
                        'Description': descr,
                        'Media': media
                        }
        if not descr and media:
            article = {
                        'Title': title,
                        'Link': link,
                        'Published': published,
                        'Media': media
                        }
        else:
            article = {
                    'Title': title,
                    'Link': link,
                    'Published': published
                    }

        article_list.append(article)

    json_data = []
    with open(Path(Path.cwd(), 'newslogjson.txt'), 'a', encoding=enc) as outfile:   # saving data to logfile in json
        if os.stat(Path(Path.cwd(), 'newslogjson.txt')).st_size == 0:
            json.dump(article_list, outfile, indent=2, ensure_ascii=False, separators=(", ", ": "))
        else:
            with open(Path(Path.cwd(), 'newslogjson.txt'), 'r', encoding=enc) as outfile1:
                json_data = json.load(outfile1)
                for i in article_list:
                    json_data.append(i)

            with open(Path(Path.cwd(), 'newslogjson.txt'), 'w', encoding=enc) as outfile2:
                json.dump(json_data, outfile2, indent=2, ensure_ascii=False, separators=(", ", ": "))

    return article_list


"""Function for getting information from log files"""


def outinfodate(date, nlimit, vrbs, js_on, enc):
    initdate = datetime.strptime(str(date), "%Y-%m-%d %H:%M:%S")
    date = datetime.strftime(initdate, "%d.%m.%Y")
    date = str(date)
    result = []
    if nlimit < 0:
        print("Limit can not be negative")
    else:
        if js_on:
            try:
                open(Path(Path.cwd(), 'newslogjson.txt'))
            except IOError as e:
                print(f"No saved data.Please, enter the url of rss")
            else:
                with open(Path(Path.cwd(), 'newslogjson.txt'), 'r', encoding="utf-8") as f:
                    json_data = json.load(f)
                    if len(json_data) == 0:
                        print('No data')
                    elif nlimit > 0 and nlimit < len(json_data):
                        numb = nlimit
                    else:
                        numb = len(json_data)
                    for i in range(numb):
                        if (json_data[i]["Published"]).startswith(date):
                            result.append(json_data[i])
                    if len(result) == 0:
                        print('No data for this date')
                    else:
                        json.dump(result, sys.stdout, indent=2, ensure_ascii=False, separators=(", ", ": "))
        else:
            try:
                open(Path(Path.cwd(), 'newslog.txt'))
            except IOError as e:
                print(f"No saved data. Please, enter the url of rss")
            else:
                with open(Path(Path.cwd(), 'newslog.txt'), 'r', encoding="utf-8") as rdr:
                    my_file = rdr.readlines()
                    a = 0
                    for i, line in enumerate(my_file):
                        if not nlimit or a < nlimit:
                            if line and line.startswith('Published: ' + date):
                                a = a + 1
                                print(my_file[(i-2)])
                                print(my_file[(i-1)])
                                print(my_file[(i)])
                                if my_file[(i+1)].startswith('Media') or my_file[(i+1)].startswith('Description'):
                                    print(my_file[(i+1)])
                                if my_file[(i+2)].startswith('Media') or my_file[(i+2)].startswith('Description'):
                                    print(my_file[(i+2)])
                                print(50*'-')
                    if a == 0:
                        print('No data for this date')


""" Main function + prints info as json in stdout"""


def fromrss(url, nlimit, vrbs=None, js_on=None, date=None):
    r = connect(url, vrbs)
    if r.encoding:
        enc = str(r.encoding)
    else:
        enc = "utf-8"
    try:
        articles, feed = out_info(r, nlimit)
    except Exception as e:
        print("No articles")
    else:
        d = detailed_info(articles, vrbs, js_on, date, feed, enc)
        if not date and js_on:
            if vrbs:
                print('Output in json format: ')
            json.dump(d, sys.stdout, indent=3, ensure_ascii=False, separators=(", ", ": "))
        if date:
            outinfodate(date, nlimit, vrbs, js_on, enc)


'''The argparse module to write user-friendly command-line interfaces.'''


def parse_news():
    parser = argparse.ArgumentParser(description='Pure Python command-line RSS reader.')
    parser.add_argument('source',  type=str, nargs='?', default=0,
                        help='RSS URL')
    parser.add_argument('--Limit', default=0, type=int, const=0, nargs='?', metavar='LIMIT',
                        help='limit news topics if this parameter provided')
    parser.add_argument('--version',  action='version', version='(Final Task)s 2.0',
                        help='Prints version info')
    parser.add_argument('--json',
                        help='Prints result at JSON in stdout', action='store_true')
    parser.add_argument('--verbose',
                        help='Outputs verbose status messages', action="store_true")
    parser.add_argument('--date',  type=lambda s: datetime.strptime(s, '%Y%m%d'), default=0,
                        help='Prints result for date entered')
    args = parser.parse_args()

    if not args.source and not args.date:
        print('Please, enter url of rss or date of saved news')
    else:
        if args.verbose:
            print("Verbose on")
            print('Starting extraction')
            if args.source:
                fromrss(args.source, args.limit, vrbs=args.verbose, js_on=args.json, date=args.date)
            if not args.source:
                outinfodate(date=args.date, nlimit=args.limit, vrbs=args.verbose, js_on=args.json, enc="utf-8")
            print('Finished extraction')
        if not args.verbose:
            if args. source:
                fromrss(args.source, args.limit, js_on=args.json, date=args.date)
            if not args. source:
                outinfodate(date=args.date, nlimit=args.limit, vrbs=args.verbose, js_on=args.json, enc="utf-8")


if __name__ == '__main__':
    parse_news()
