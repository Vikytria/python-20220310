import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LocationsMainPage: 
    def __init__(self, driver) -> None:             #Elmenti a driver meghívását egy globális változóba -> innentől csak erre kell hivatkozni
        self.driver = driver                        #Első paraméter mindig a 'self'

    def open(self):
        self.driver.get("http://localhost:8080")
        return self

    def click_create_location_link(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "create-location-link"))
        )
        link = self.driver.find_element(By.ID, "create-location-link")
        link.click()
        return self
    
    def fill_form_all(self, name: str = "Home", coords: str = "1,1", interesting_at: str = "", tags: str = ""):
        """Kitölti az űrlapot névvel, koordinátákkal stb"""
        name_input = self.driver.find_element(By.ID, "location-name").send_keys(name)
        coords_input = self.driver.find_element(By.ID, "location-coords").send_keys(coords)
        interesting_at_input = self.driver.find_element(By.ID, "location-interesting-at").send_keys(interesting_at)
        tags_input = self.driver.find_element(By.ID, "location-tags").send_keys(tags)
        return self

    def click_create_location_button(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        return self

    def assert_text_on_message_panel(self, text):
        message_div = self.driver.find_element(By.ID, "message-div")
        assert message_div.text == text
        return self
    
    def assert_text_on_error_message(self, text):
        error_div = self.driver.find_element(By.CSS_SELECTOR, ".invalid-feedback:not([hidden='hidden'])")
        assert error_div.text == text
        return self
    

    
