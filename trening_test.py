import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.basic
def test_trening360(driver: WebDriver, base_url): 
    driver.get(base_url)
    driver.save_screenshot("main.png")
    title = driver.title
    assert "informatikai tanfolyamok" in title.lower()

def test_elementscrenshoot(driver: WebDriver, base_url):
    driver.get(base_url)
    newsletter_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "NewsletterModalCloseButton"))
    )
    newsletter_button.click()
    driver.find_element(By.CSS_SELECTOR, ".cookie__button").click()
    element = driver.find_element(By.CSS_SELECTOR, "[data-href='/irodai-informatika']")
    element.screenshot("button.png")



