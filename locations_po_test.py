from LocationsMainPage import LocationsMainPage
import requests
import mariadb

def test_crerate(driver):
    # requests.delete("http://localhost:8080/api/locations")    # APIn át való adatbázis törlés

    conn = mariadb.connect(user="locations", password="locations", host="localhost", database="locations")
    cur = conn.cursor()
    cur.execute("delete from location")
    conn.commit()
    conn.close()

    page = LocationsMainPage(driver)
    page.open() \
        .click_create_location_link() \
        .fill_form_all() \
        .click_create_location_button() \
        .assert_text_on_message_panel("Location has been created")
    print("end")

def test_empty_name(driver):
    page = LocationsMainPage(driver)
    page.open() \
        .click_create_location_link() \
        .fill_form_all("") \
        .click_create_location_button() \
        .assert_text_on_error_message("Can not be empty name!")
    print("end")

def test_empty_coords(driver):
    page = LocationsMainPage(driver)
    page.open()
    page.click_create_location_link()
    page.fill_form_all(coords="")           #csak az adott paraméternek írja felül a default értékét
    page.click_create_location_button() 
    page.assert_text_on_error_message("Invalid format!")
    print("end")

def test_big_data(driver):
    page = LocationsMainPage(driver)
    page.open()

    with open("MOCK_DATA.csv", encoding='utf-8') as f: 
        for line in f: 
            parts = line.strip().split(",")
            page.click_create_location_link()
            page.fill_form_all(parts[0], parts[1] + "," + parts[2])
            page.click_create_location_button() 


