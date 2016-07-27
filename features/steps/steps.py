import time

@when('visit url "{url}"')
def step(context, url):
    context.browser.get(url)

@when('field with name "{selector}" is given "{value}"')
def step(context, selector, value):
    elem = context.browser.find_element_by_name(selector)
    elem.send_keys(value)
    elem.submit()
    time.sleep(5)

@then('title becomes "{title}"')
def step(context, title):
    assert context.browser.title == title

@then(u'page contains "{body}"')
def step(context, body):
    assert body in context.browser.page_source
