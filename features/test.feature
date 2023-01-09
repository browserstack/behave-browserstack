Feature: Google\'s Search Functionality
    Scenario: can find search results
        When visit url "http://www.google.com/ncr"
        When field with name "q" is given "BrowserStack"
        Then title becomes "BrowserStack - Google Search"
