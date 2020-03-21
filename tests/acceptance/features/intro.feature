Feature: Navigate to the OWASP Juice shop Page

  Scenario: Create a new account
    Given I navigate to the OWASP homepage
    And I remove all the popups
    And I click on the account link
    When I click on the login link
    Then I will be on the login page
    When I click on the new customer link
    Then I will be on the user registration page
    When I input data into the mandatory field
    Then I will be on the login page

