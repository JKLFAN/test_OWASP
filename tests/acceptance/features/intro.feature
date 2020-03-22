Feature: Navigate to the OWASP Juice shop Page

  Background:
    Given I navigate to the OWASP homepage
    And I remove all the popups

  Scenario: Create a new account
    When I click on the account link
    And I click on the login link
    Then I will be on the login page
    When I click on the new customer link
    Then I will be on the user registration page
    When I input data into the mandatory field
    Then I will be on the login page

  Scenario: Assert the presence of products
    Then the page will show the "Apple Juice (1000ml)" product
    And the page will show the "Apple Pomace" product
    And the page will show the "Banana Juice (1000ml)" product
    And the page will show the "Carrot Juice (1000ml)" product
    And the page will show the "Eggfruit Juice (500ml)" product




