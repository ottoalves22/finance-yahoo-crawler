from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


description = """

### Stock Crawler and Scraper

Will generate an CSV file with stocks data from given country.
"""

app = FastAPI(title='Stock Crawler and Scraper', description=description, version='1.0.0', docs_url='/docs')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate_stock_csv")
async def get_stock_csv():
    return {"message": "Hello World"}