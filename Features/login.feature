Feature: Login in OrangeHRM

  @login_valid
  Scenario: Login with valid credentials
    Given I got navigated to OrangeHRM
    When I enter username
    And I enter password
    And Click on login
    Then User should land onto Homepage

  @login_Invalid
  Scenario Outline: Login with invalid credentials
    Given I got navigated to OrangeHRM
    When I enter '<username>'
    And I enter '<password>'
    And Click on login
    Then User should see "Invalid credentials"
    Examples:
      |username  |password|
      |adm        |    12    |

