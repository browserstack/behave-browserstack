# behave-browserstack

[Behave](http://pythonhosted.org/behave/) Integration with BrowserStack.

## Setup

- Clone the repo
- Install dependencies `pip install -r requirements.txt`
- Update `*.json` files inside the `config/` directory with your BrowserStack Username and Access Key. (These can be found in the [settings](https://www.browserstack.com/accounts/settings) section on BrowserStack accounts page)
- Alternatively, you can export the environment variables for the Username and Access Key of your BrowserStack account.
```
export BROWSERSTACK_USERNAME=<browserstack-username>
export BROWSERSTACK_ACCESS_KEY=<browserstack-access-key>
```

### Run the tests

- To run single test, run `paver run single`
- To run parallel tests, run `paver run parallel`
- To run local tests, run `paver run local`

### Notes

- In order to test on different set of browsers, check out our [code generator](https://www.browserstack.com/automate/python#setting-os-and-browser)
