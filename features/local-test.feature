Feature: BStack Local Testing
    Scenario: can check tunnel working
        When visit url "http://bs-local.com:45454/"
        Then title contains "BrowserStack Local"
