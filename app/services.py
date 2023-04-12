from services_modules.crawler import Crawler 
from services_modules.scraper import Scraper

# The region parameter needs to be according to yahoo finances regions list
region = 'Qatar'

class ScrapreCrawlerService:
    def generate_stocks_data(self, region: str):
        crawler = Crawler()
        finance_table_html = crawler.crawl_finances(region)
        scraper = Scraper()
        scraper.generate_files(finance_table_html)

