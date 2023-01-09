from selenium import webdriver

def before_feature(context, feature):
    desired_capabilities = {
        'browserName': 'chrome'
    }
    context.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://localhost:4444/wd/hub"
    )

def after_feature(context, feature):
    context.browser.quit()
