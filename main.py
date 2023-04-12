from crawler import Crawler 
from scraper import Scraper

# The region parameter needs to be according to yahoo finances regions list
region = 'Qatar'

crawler = Crawler()
finance_table_html = crawler.crawl_finances(region)
scraper = Scraper()
scraper.generate_files(finance_table_html)
