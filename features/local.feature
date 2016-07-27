Feature: BrowserStack Local Testing
    Scenario: can check tunnel working
        When visit url "http://bs-local.com:45691/check"
        Then page contains "Up and running"
