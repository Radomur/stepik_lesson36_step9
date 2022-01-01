link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_presence_of_basket_button(browser):
    browser.get(link)
    assert browser.find_element_by_css_selector("button.btn-add-to-basket"), "button not found"
