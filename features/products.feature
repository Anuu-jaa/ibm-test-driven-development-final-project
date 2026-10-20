Feature: Product management
  As a product manager
  I want to manage products
  So that I can maintain the product catalog

  Scenario: Read a product
    When I visit the "Home Page"
    And I enter "Hat" in the "Name" field
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Hat" in the results
    When I copy the ID of the "Hat" product
    And I press the "Clear" button
    And I paste the copied ID into the "Product ID" field
    And I press the "Retrieve" button
    Then I should see the message "Success"
    And I should see "Hat" in the "Name" field
    And I should see "A red fedora" in the "Description" field

  Scenario: Update a product
    When I visit the "Home Page"
    And I enter "Hat" in the "Name" field
    And I press the "Search" button
    Then I should see "Hat" in the results
    When I copy the ID of the "Hat" product
    And I press the "Clear" button
    And I paste the copied ID into the "Product ID" field
    And I enter "Fedora" in the "Name" field
    And I press the "Update" button
    Then I should see the message "Product updated"
    When I press the "Clear" button
    And I enter "Fedora" in the "Name" field
    And I press the "Search" button
    Then I should see "Fedora" in the results
    And I should not see "Hat" in the results

  Scenario: Delete a product
    When I visit the "Home Page"
    And I enter "Hat" in the "Name" field
    And I press the "Search" button
    Then I should see "Hat" in the results
    When I copy the ID of the "Hat" product
    And I press the "Clear" button
    And I paste the copied ID into the "Product ID" field
    And I press the "Delete" button
    Then I should see the message "Product has been Deleted!"
    When I press the "Clear" button
    And I enter "Hat" in the "Name" field
    And I press the "Search" button
    Then I should not see "Hat" in the results

  Scenario: List all products
    When I visit the "Home Page"
    And I press the "Clear" button
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Hat" in the results
    And I should see "Shoes" in the results
    And I should see "Big Mac" in the results
    And I should see "Sheets" in the results

  Scenario: Search products by category
    When I visit the "Home Page"
    And I press the "Clear" button
    And I select "Food" from the "Category" dropdown
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Big Mac" in the results
    And I should not see "Shoes" in the results
    And I should not see "Sheets" in the results

  Scenario: Search products by availability
    When I visit the "Home Page"
    And I press the "Clear" button
    And I select "True" from the "Available" dropdown
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Hat" in the results
    And I should see "Big Mac" in the results
    And I should see "Sheets" in the results
    And I should not see "Shoes" in the results

  Scenario: Search products by name
    When I visit the "Home Page"
    And I enter "Hat" in the "Name" field
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Hat" in the "Name" field
    And I should see "A red fedora" in the "Description" field