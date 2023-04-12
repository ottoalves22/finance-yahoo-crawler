from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .services import ScraperCrawlerService
from fastapi.responses import FileResponse

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

@app.on_event("startup")
async def startup():
    global robot_svc
    robot_svc = ScraperCrawlerService()

@app.get("/generate_stock_csv/region",
         tags=['scrapping'],
          description="""Collect data about stocks of given country (region) and return in a CSV file.
            The parameter region must be written in english and capital letters.
            Depending on the country the list can be long and it may take a while.""",
          responses={
            200: {
                "description": "Returns brand new CSV file with collected stocks data.",
            }
          })
async def get_stock_csv(region: str):
    global robot_svc
    csv_path = robot_svc.generate_stocks_data(region)
    return FileResponse(csv_path)
