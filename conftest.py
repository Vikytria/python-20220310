import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service      # Edge: edge.service
from webdriver_manager.chrome import ChromeDriverManager   # .microsoft / edgedrivermanager
from selenium.webdriver.chrome.options import Options
# chromet konfigurálni kell h zavaro ablakok ne ugorjanak fel

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    #driver.get(base_url)
    return driver

