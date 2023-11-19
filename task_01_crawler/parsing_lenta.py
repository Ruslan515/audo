#!/usr/bin/python3
"""
parsing lenta.ru
"""
# from .. lib.crawler import CrawlerRuslan
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from my_lib.crawler import CrawlerRuslan

def main():
    crawler = CrawlerRuslan()
    crawler.crawling()


if __name__ == "__main__":
    main()
