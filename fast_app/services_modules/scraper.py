from datetime import datetime
import json
from bs4 import BeautifulSoup
import csv

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
    
    def generate_csv_file(self, finance_dict: list) -> str:
        keys = finance_dict[0].keys()
        filaname = f'yahoo_finances_{datetime.now()}.csv' 
        with open(filaname, 'w', newline='') as csv_file:
            dict_writer = csv.DictWriter(csv_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(finance_dict)
            return filaname

    def generate_files(self, finance_table_html: list) -> str:
        finance_dicts = self.generate_json(finance_table_html)
        filename = self.generate_csv_file(finance_dicts)
        return filename
                