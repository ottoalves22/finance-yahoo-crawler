from datetime import datetime
import json
from bs4 import BeautifulSoup

class Scraper:
    def generate_json(self, html: list) -> dict:
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

        json_object = json.dumps(final_dict_list, indent=4)
        with open(f"yahoo_finances_{datetime.now()}.json", 'w') as out_file:
            out_file.write(json_object)

        return final_dict_list
                