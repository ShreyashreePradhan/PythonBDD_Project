Feature: Login in OrangeHRM

  @login_valid
  Scenario: Login with valid credentials
    Given I got navigated to OrangeHRM
    When I enter username as "Admin"
    And I enter password as "admin123"
    And I click on login
    Then I should see "Dashboard" in homepage

  @login_Invalid
  Scenario Outline: Login with invalid credentials
    Given I got navigated to OrangeHRM
    When I enter invalid username as "<username>"
    And I enter invalid password as "<password>"
    And I click on login
    Then I should see "Invalid credentials" in loginpage
    Examples:
      |username  |password|
      |adm        |    12    |
      |13           |     89     |

