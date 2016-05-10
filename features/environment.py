import os
from selenium import webdriver
from browserstack.local import Local

# Edit these to match your credentials
USERNAME = None
BROWSERSTACK_KEY = None
test_type = 'single'
bs_local = None

if "BROWSERSTACK_USERNAME" in os.environ:
    USERNAME = os.environ["BROWSERSTACK_USERNAME"]
if "BROWSERSTACK_ACCESS_KEY" in os.environ:
    BROWSERSTACK_KEY = os.environ["BROWSERSTACK_ACCESS_KEY"]
if "TEST_TYPE" in os.environ:
    test_type = os.environ["TEST_TYPE"]

if not (USERNAME and BROWSERSTACK_KEY):
    raise Exception("Please provide your BrowserStack username and access key")
    sys.exit(1)

def start_local():
    global bs_local
    bs_local = Local()
    bs_local_args = { "key": BROWSERSTACK_KEY, "forcelocal": "true" }
    bs_local.start(**bs_local_args)

def stop_local():
    global bs_local
    if bs_local is not None:
        bs_local.stop()

def get_caps():
    desired_capabilities = {}
    desired_capabilities['os'] = 'OS X'
    desired_capabilities['os_version'] = 'El Capitan'
    desired_capabilities['browser'] = 'firefox'
    desired_capabilities['browser_version'] = '46'
    desired_capabilities['build'] = 'Sample behave tests'
    desired_capabilities['name'] = 'Sample behave test'
    if 'local' in test_type.lower():
        desired_capabilities['browserstack.local'] = True
    return desired_capabilities

def before_feature(context, feature):
    if 'parallel' in test_type.lower():
        context.browser = create_driver()

def after_feature(context, feature):
    if 'parallel' in test_type.lower():
        context.browser.quit()

def before_all(context):
    if 'local' in test_type.lower():
        start_local()
    if 'parallel' not in test_type.lower():
        context.browser = create_driver()

def after_all(context):
    stop_local()
    if 'parallel' not in test_type.lower():
        context.browser.quit()

def create_driver():
    desired_capabilities = get_caps()

    return webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://%s:%s@hub.browserstack.com/wd/hub" % (
                USERNAME, BROWSERSTACK_KEY
                )
            )
