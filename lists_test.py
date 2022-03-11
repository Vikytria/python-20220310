from lib2to3.pgen2 import driver
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def open_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:5500/Docs/index.html")
    return driver

def get_list_items(driver):
    elements = driver.find_elements(By.TAG_NAME, "li")
    print(elements)
    items = []
    for element in elements:
        items.append(element.text)
    return items

def test_list():
    driver = open_page()
    items = get_list_items(driver)
    assert items == ["Python", "HTML", "CSS"]
