# behave-browserstack

[Behave](http://pythonhosted.org/behave/) Integration with BrowserStack.

![BrowserStack Logo](https://d98b8t1nnulk5.cloudfront.net/production/images/layout/logo-header.png?1469004780)

## Setup

* Clone the repo
* Install dependencies `pip install -r requirements.txt`
* Update `*.json` files inside the `config/` directory with your [BrowserStack Username and Access Key](https://www.browserstack.com/accounts/settings)

## Running your tests
* To run a single test, run `paver run single`
* To run parallel tests, run `paver run parallel`
* To run local tests, run `paver run local`

## Notes
* You can view your test results on the [BrowserStack automate dashboard](https://www.browserstack.com/automate)
* To test on a different set of browsers, check out our [platform configurator](https://www.browserstack.com/automate/python#setting-os-and-browser)
* You can export the environment variables for the Username and Access Key of your BrowserStack account
  
  ```
  export BROWSERSTACK_USERNAME=<browserstack-username> &&
  export BROWSERSTACK_ACCESS_KEY=<browserstack-access-key>
  ```
  
## Additional Resources
* [Documentation for writing automate test scripts in Python](https://www.browserstack.com/automate/python)
* [Customizing your tests on BrowserStack](https://www.browserstack.com/automate/capabilities)
* [Browsers & mobile devices for selenium testing on BrowserStack](Browsers & Mobile Devices for Selenium Testing)
* [Using REST API to access information about your tests via the command-line interface](https://www.browserstack.com/automate/rest-api)
