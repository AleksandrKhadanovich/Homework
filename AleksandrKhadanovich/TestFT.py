import unittest
import rss_reader
import requests
import sys


class TestParse(unittest.TestCase):
    
    def test_connect(self):
        argin1 = "https://www.yahoo.com/news/rss"
        a = (rss_reader.connect(argin1)).status_code
        self.assertEqual(a,200)

        
    def test_connect1(self):
        argin2 = "https://www.yahoo.com/ws/rss"
        a = (rss_reader.connect(argin2)).status_code
        self.assertNotEqual(a,200)


    def test_outinfo(self):
        argin3 = "https://www.yahoo.com/news/rss"
        r= requests.get(argin3)
        nlimit=5        
        n=rss_reader.out_info(r,nlimit)
        self.assertEqual(nlimit,len(n))
       
        
    def test_detailed_info(self):
        argin = "https://www.yahoo.com/news/rss"
        r= requests.get(argin)
        nlimit=5        
        n=rss_reader.out_info(r,nlimit)
        a= rss_reader.detailed_info(n, vrbs=None, js_on=1)
        self.assertEqual(['Title', 'Link', 'Published'],list(a[0].keys()))


    def test_detailed_info2(self):
        argin = "https://www.yahoo.com/news/rss"
        r= requests.get(argin)
        nlimit=5        
        n=rss_reader.out_info(r,nlimit)        
        a= rss_reader.detailed_info(n, vrbs=None, js_on=1)
        self.assertEqual(len(n),len(a))

     
if __name__ == '__main__':
    unittest.main()        
               
