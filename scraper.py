from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, html: list) -> None:
        for h in html:
            soup = BeautifulSoup(h, "html.parser")
            for x in soup.find_all("a"):
            #    print(x)
                pass
                