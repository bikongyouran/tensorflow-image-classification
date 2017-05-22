#-*- coding:utf-8 -*-
from icrawler.builtin import GoogleImageCrawler


google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                    storage={'root_dir': 'C:\codes\\tensorflow-doc-dataset\\US_PP2'})
google_crawler.crawl(keyword='valid passport US jpg', offset=0, max_num=1000,
                     date_min=None, date_max=None,
                     min_size=(200,200), max_size=None)