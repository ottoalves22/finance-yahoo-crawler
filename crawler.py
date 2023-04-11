from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup




class Crawler:
    start_url = "https://finance.yahoo.com/screener/new"

    def __init__(self) -> None:
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--log-level=3")
        chrome_options.binary_location = '/usr/bin/google-chrome'
        download_dir = './'
        chrome_options.add_experimental_option('prefs', {"download.default_directory": download_dir,
                                                        "download.prompt_for_download": False,
                                                        "download.directory_upgrade": True,
                                                        "plugins.always_open_pdf_externally": True
                                                        })

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
