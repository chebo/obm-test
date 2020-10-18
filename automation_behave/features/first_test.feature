Feature: First test

Scenario: Run a simple test
    Given I open http://openbodymind.com/ using chrome
    When I have 6 links within school menu items using chrome
    Then I take screenshot using chrome

Scenario: Check of students examination results
    Given I open http://openbodymind.com/articles/testing/ using chrome
    When I have read list of students items using chrome
    Then I take screenshot using chrome
