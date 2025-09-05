  Scenario: Read a Product
    Given the following products
      | name  | category | available | price |
      | Apple | Food     | True      | 1.50  |
    When I retrieve "Apple"
    Then I should see the product "Apple" with category "Food" and price 1.50 and availability "True"

      Scenario: Update a Product
    Given the following products
      | name  | category | available | price |
      | Banana | Food     | True      | 0.75  |
    When I update "Banana" to category "Fruit" and price 0.80 and availability "False"
    Then I should see the product "Banana" with category "Fruit" and price 0.80 and availability "False"

  Scenario: Delete a Product
    Given the following products
      | name  | category | available | price |
      | Orange | Food     | True      | 1.20  |
    When I delete "Orange"
    Then I should not see "Orange"

  Scenario: List all Products
    Given the following products
      | name  | category | available | price |
      | Product A | Category X | True | 10.00 |
      | Product B | Category Y | False | 20.00 |
      | Product C | Category X | True | 30.00 |
    When I list all products
    Then I should see 3 products
    And I should see "Product A"
    And I should see "Product B"
    And I should see "Product C"

  Scenario: Search Products by Name
    Given the following products
      | name  | category | available | price |
      | Laptop | Electronics | True | 1200.00 |
      | Mouse | Electronics | True | 25.00 |
    When I search for products by name "Laptop"
    Then I should see 1 product
    And I should see "Laptop"
    But I should not see "Mouse"

  Scenario: Search Products by Category
    Given the following products
      | name  | category | available | price |
      | T-Shirt | Clothes | True | 15.00 |
      | Jeans | Clothes | True | 40.00 |
      | TV | Electronics | True | 500.00 |
    When I search for products by category "Clothes"
    Then I should see 2 products
    And I should see "T-Shirt"
    And I should see "Jeans"
    But I should not see "TV"

  Scenario: Search Products by Availability
    Given the following products
      | name  | category | available | price |
      | Available Item | Test | True | 5.00 |
      | Unavailable Item | Test | False | 6.00 |
    When I search for products by availability "True"
    Then I should see 1 product
    And I should see "Available Item"
    But I should not see "Unavailable Item"
