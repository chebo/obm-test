Feature: First test

Scenario: Run a simple test
    Given I open http://openbodymind.com/ using chrome
    When I have 6 links within school menu items using chrome
    Then I take screenshot using chrome
