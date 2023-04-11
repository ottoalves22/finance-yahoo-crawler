from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
        # For debugging the browser:
        chrome_options.add_experimental_option("detach", True)


        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    def crawl_finances(self, region: str):
        self.driver.get(self.start_url)
        # by default Region will include United States. The next action will be removing the default value
        default_value_bt = self.driver.find_element(By.XPATH, '//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li[1]/button')
        default_value_bt.click()

        add_region_bt = self.driver.find_element(By.XPATH, '//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li/div/div')
        add_region_bt.click()

        add_region_input = self.driver.find_element(By.XPATH, '//*[@id="dropdown-menu"]/div/div[1]/div/input')
        add_region_input.send_keys(region)
        region_ckbx = self.driver.find_element(By.XPATH, '//*[@id="dropdown-menu"]/div/div[2]/ul/li/label')
        self.driver.implicitly_wait(15)
        region_ckbx.send_keys(Keys.SPACE)
        