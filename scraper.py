from bs4 import BeautifulSoup

class Scraper:
    def generate_dict(self, html: list) -> dict:
        final_dict_list = []
        for h in html:
            soup = BeautifulSoup(h, "html.parser")
            for x in soup.find_all("a"):
                name = x['title']
                symbol = x.get_text()
                price_intraday = float(soup.select_one(f'fin-streamer[data-symbol="{symbol}"]').get_text())
                final_dict_list.append({
                    "Name": name,
                    "Symbol": symbol,
                    "Price Intraday": price_intraday
                })
        
        return final_dict_list

                