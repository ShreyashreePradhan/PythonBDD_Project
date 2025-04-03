Feature: Search in OrangeHRM
 @search
  Scenario: Search after login
    Given I logged in to OrangeHRM
    When I search "Leave"
    Then I only see "Leave" module