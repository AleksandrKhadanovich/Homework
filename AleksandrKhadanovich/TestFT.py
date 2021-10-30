import unittest
import rss_reader
import requests
import sys
from unittest.mock import patch
import sys
from pathlib import Path
import io
import datetime


class TestParse(unittest.TestCase):

    def test_connect(self):
        argin1 = "https://www.yahoo.com/news/rss"
        a = (rss_reader.connect(argin1)).status_code
        self.assertEqual(a, 200)

    def test_connect1(self):
        argin2 = "https://www.yahoo.com/ws/rss"
        a = (rss_reader.connect(argin2)).status_code
        self.assertNotEqual(a, 200)

    def test_outinfo(self):
        argin3 = "https://www.yahoo.com/news/rss"
        r = requests.get(argin3)
        nlimit = 5
        n, v = rss_reader.out_info(r, nlimit)
        self.assertEqual(nlimit, len(n))

    def test_detailed_info(self):
        argin = "https://www.yahoo.com/news/rss"
        r = requests.get(argin)
        nlimit = 5
        n, v = rss_reader.out_info(r, nlimit)
        a = rss_reader.detailed_info(n, vrbs=None, js_on=1, date=None, feed=' ', enc='utf-8', path1=None, path2=None)
        self.assertEqual(['Title', 'Link', 'Published', 'Media'], list(a[0].keys()))

    def test_detailed_info3(self):
        argin = "https://www.yahoo.com/news/rss"
        r = requests.get(argin)
        nlimit = 1
        n, v = rss_reader.out_info(r, nlimit)
        rss_reader.detailed_info(n, vrbs=None, js_on=1, date=None, feed=' ', enc='utf-8', path1=None, path2=None)
        path = Path(Path.cwd(), 'newslogjson.txt')
        assert path.is_file()

    def test_detailed_info2(self):
        argin = "https://www.yahoo.com/news/rss"
        r = requests.get(argin)
        nlimit = 5
        n, v = rss_reader.out_info(r, nlimit)
        a = rrss_reader.detailed_info(n, vrbs=None, js_on=1, date=None, feed=' ', enc='utf-8', path1=None, path2=None)
        self.assertEqual(len(n), len(a))

    def test_date_convert1(self):
        a = rss_reader.date_convert('2021-10-27T15:03:59Z')
        self.assertEqual(a, '27.10.2021 15:03:59')

    def test_date_convert2(self):
        a = rss_reader.date_convert('Tue, 26 Oct 2021 19:14:39 GMT')
        self.assertEqual(a, '26.10.2021 19:14:39')

    def test_date_convert3(self):
        a = rss_reader.date_convert('Tue, 26 Oct 2021 22:14:10 +0300')
        self.assertEqual(a, '26.10.2021 22:14:10')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_outinfo2(self, mockstd):
        rss_reader.outinfodate('2021-10-21 22:14:10', nlimit=-1, vrbs=None, js_on=1, enc='utf-8', path1=None, path2=None)
        self.assertEqual(mockstd.getvalue(), "Limit can not be negative\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_outinfo3(self, mockstd):
        argin = "https://www.yahoo.com/news/rss"
        r = requests.get(argin)
        nlimit = 0
        n, v = rss_reader.out_info(r, nlimit)
        rss_reader.detailed_info(n, vrbs=None, js_on=1, date=None, feed=' ', enc='utf-8', path1=None, path2=None)
        rss_reader.outinfodate('1021-10-21 22:14:10', nlimit=0, vrbs=None, js_on=1, enc='utf-8', path1=None, path2=None)
        self.assertEqual(mockstd.getvalue(), "No data for this date\n")

    def test_detailedinfo_pdf(self):
        argin = "https://www.yahoo.com/news/rss"
        r = requests.get(argin)
        nlimit = 5
        n, v = rss_reader.out_info(r, nlimit)
        pth = Path(Path.cwd(), 'tstfile.pdf')
        rss_reader.detailed_info(n, vrbs=None, js_on=1, date=None, feed=' ', enc='utf-8', path1=None, path2=pth)
        self.assertEqual((str(pth), pth.is_file()), (str(pth), True))
        pth.unlink()

    def test_detailedinfo_html(self):
        argin = "https://www.yahoo.com/news/rss"
        r = requests.get(argin)
        nlimit = 5
        n, v = rss_reader.out_info(r, nlimit)
        pth = Path(Path.cwd(), 'tstfile.html')
        rss_reader.detailed_info(n, vrbs=None, js_on=1, date=None, feed=' ', enc='utf-8', path1=pth, path2=None)
        self.assertEqual((str(pth), pth.is_file()), (str(pth), True))
        pth.unlink()

    def test_outtohtml(self):
        argin = "https://www.yahoo.com/news/rss"
        r = requests.get(argin)
        nlimit = 5
        n, v = rss_reader.out_info(r, nlimit)
        rss_reader.detailed_info(n, vrbs=None, js_on=1, date=None, feed=' ', enc='utf-8', path1=None, path2=None)
        path = Path(Path.cwd(), 'testfilehtml.html')
        now = datetime.datetime.now()
        datenow = now.strftime("%d.%m.%Y")
        rss_reader.outtohtml(path, nlimit, date=datenow)
        self.assertEqual((str(path), path.is_file()), (str(path), True))
        path.unlink()

    def test_outtopdf(self):
        argin = "https://www.yahoo.com/news/rss"
        r = requests.get(argin)
        nlimit = 5
        n, v = rss_reader.out_info(r, nlimit)
        rss_reader.detailed_info(n, vrbs=None, js_on=1, date=None, feed=' ', enc='utf-8', path1=None, path2=None)
        path = Path(Path.cwd(), 'testfilepdf.pdf')
        now = datetime.datetime.now()
        datenow = now.strftime("%d.%m.%Y")
        rss_reader.outtopdf(path, nlimit, date=datenow)
        self.assertEqual((str(path), path.is_file()), (str(path), True))
        path.unlink()
        Path(Path.cwd(), 'newslog.txt').unlink()
        Path(Path.cwd(), 'newslogjson.txt').unlink()


if __name__ == '__main__':
    unittest.main()
