# finance-yahoo-crawler

This app will crawl the site https://finance.yahoo.com/screener/new using as parameter one Region then crawling data like Symbol, Name and Price (Intraday).
These variables are collected and stored as a JSON file, which can be exported as a CSV file.
Built on linux environment, chromedrive might differ.
Access it using fastapi documentation

## Local Execution
```bash
pip install -r requirements.txt && ./run.sh
```

## Docker Execution
```bash
sudo ./docker.sh --build

sudo ./docker.sh --start

sudo ./docker.sh --stop

sudo ./docker.sh --restart
```
Flag restart will stop, prune containers and start a new one

## Documentation

Access http://127.0.0.1:8000/docs after running the commands above