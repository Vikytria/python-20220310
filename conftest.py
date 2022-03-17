import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service      # Edge: edge.service
from webdriver_manager.chrome import ChromeDriverManager   # .microsoft / edgedrivermanager

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #driver.get(base_url)
    return driver

