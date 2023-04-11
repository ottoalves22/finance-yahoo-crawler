from crawler import Crawler 

crawler = Crawler()
# The region parameter needs to be according to yahoo finances regions list
region = 'Brazil'
crawler.crawl_finances(region)
print("Hello World")
