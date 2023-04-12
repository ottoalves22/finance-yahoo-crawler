# finance-yahoo-crawler

This app will crawl the site https://finance.yahoo.com/screener/new using as parameter one Region then crawling data like Symbol, Name and Price (Intraday).
These variables are collected and stored as a JSON file, which can be exported as a CSV file.
Built on linux environment, chromedrive might differ.
Access it using fastapi documentation

## Execution
```bash
pip install -r requirements.txt && ./run.sh
```

## Documentation

Access http://127.0.0.1:8000/docs after running the commands above