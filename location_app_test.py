import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

test_city = "Zamárdi"
test_coords = "1,1"
test_interestin_at = "2019-09-11T15:31:04"
test_tags = ["interesting city", "balatoni város", "Szép hely"]

def test_location_create(driver: WebDriver, base_url):
    driver.get(base_url)
    driver.find_element(By.ID, "create-location-link").click()

    driver.find_element(By.ID, "location-name").send_keys(test_city)
    driver.find_element(By.ID, "location-coords").send_keys(test_coords)
    driver.find_element(By.ID, "location-interesting-at").send_keys(test_interestin_at)
    driver.find_element(By.ID, "location-tags").send_keys(test_tags)

    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    create_result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message-div"))
    )
    created_success = driver.find_element(By.ID, "message-div").text
    assert "Location has been created" in created_success

    driver.find_element(By.ID, "refresh-button").click()

    create_result_table = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "locations-table"), "AAA_Szeged")
    )

    location_name = driver.find_element(By.ID, "locations-table").text
    assert test_city in location_name

def test_location_delete(driver: WebDriver, base_url):
    driver.get(base_url)

    first_line_id = driver.find_element(By.CSS_SELECTOR, "#locations-table-tbody > tr:nth-child(1) > td:nth-child(1)").text
    driver.find_element(By.CSS_SELECTOR, "tbody td .btn-danger").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#delete-location-form > p:nth-child(3) > input.btn.btn-danger"))
    )
    driver.find_element(By.CSS_SELECTOR, "#delete-location-form > p:nth-child(3) > input.btn.btn-danger").click()

    driver.find_element(By.ID, "refresh-button").click()

    new_first_line_id = driver.find_element(By.CSS_SELECTOR, "#locations-table-tbody > tr:nth-child(1) > td:nth-child(1)").text
    assert new_first_line_id not in first_line_id

