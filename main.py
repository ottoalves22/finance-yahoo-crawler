from crawler import Crawler 

crawler = Crawler()
# The region parameter needs to be according to yahoo finances regions list
region = 'Brazil'
finance_table_html = crawler.crawl_finances(region)
