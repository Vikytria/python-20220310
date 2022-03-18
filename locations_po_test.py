from LocationsMainPage import LocationsMainPage

def test_crerate(driver):
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



