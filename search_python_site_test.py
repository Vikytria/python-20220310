from urllib.parse import urljoin
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

@pytest.mark.fn_search    #markerek megadása
@pytest.mark.basic
def test_search_pep(driver: WebDriver, base_url): 
    driver.get(base_url)
    driver.find_element(By.ID, "id-search-field").send_keys("pep")
    driver.find_element(By.ID, "submit").click()

    first_result = driver.find_element(By.CSS_SELECTOR, "#content > div > section > form > ul > li:nth-child(1) > h3 > a").text
    assert "pep" in first_result.lower()

def test_about(driver, base_url):
    driver.get(urljoin(base_url, "/about/"))
    
    title = driver.title
    assert "about" in title.lower()

    # base_url -eket a tesztesetekben definiáljuk mert lehetséges hogy nem ugyan azon az url-en kell mennie a tesztnek4
    # base_url értékét a pytest.ini fájlbol olvassa be 
    # ha parancssorbol inditjuk akkor az fog futni