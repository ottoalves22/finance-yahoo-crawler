from crawler import Crawler 
from scraper import Scraper

crawler = Crawler()
# The region parameter needs to be according to yahoo finances regions list
region = 'Qatar'
finance_table_html = crawler.crawl_finances(region)
scraper = Scraper()
finance_dicts = scraper.generate_json(finance_table_html)