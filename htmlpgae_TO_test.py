import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_showlivealert(driver: WebDriver, base_url):
    driver.get(base_url)
    driver.find_element(By.ID, "liveAlertBtn").click()
    alert_success = driver.find_element(By.CSS_SELECTOR, ".alert-success").text

    assert "Nice" in alert_success

def test_showlivealert_TO(driver: WebDriver, base_url):
    driver.get(base_url)
    driver.find_element(By.ID, "liveAlertTimeoutBtn").click()
    alert_success_TO = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message-div"))
    )
    alert_success = driver.find_element(By.CSS_SELECTOR, ".alert-success").text

    assert "Location has been created" in alert_success
