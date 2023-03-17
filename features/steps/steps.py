import time
from selenium.webdriver.common.by import By

@when('visit url "{url}"')
def step(context, url):
    context.browser.get(url)
    time.sleep(2)
    
@when("item with xpath '{selector}' is present to be added to cart")
def step(context, selector):
    item = context.browser.find_element(By.XPATH, selector)
    context.item_to_add = item.text

@when("add to cart button '{selector}' for above item is clicked")
def step(context, selector):
    add_btn = context.browser.find_element(By.XPATH, selector)
    add_btn.click()
    time.sleep(2)

@then("item in cart '{selector}' is same as the one which was added")
def step(context, selector):
    item = context.browser.find_element(By.XPATH, selector)
    item_in_cart = item.text
    assert item_in_cart == context.item_to_add

@then('title contains "{title}"')
def step(context, title):
    assert title in context.browser.title
