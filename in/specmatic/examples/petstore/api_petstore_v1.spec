Feature: Contract for the petstore service
  Background:
    Given json Pet
      | name   | (string) |
      | type   | (string) |
      | status | (string) |
      | id     | (number) |
    And json Pets (Pet*)
    And json Order
      | type   | (string) |
      | count  | (number) |
      | status | (string) |
      | id     | (number) |
    And json Orders (Order*)
    And value auth from auth.spec

  Scenario Outline: Fetch pet details
    When GET /pets/(id:number)
    Then status 200
    And response-body (Pet)
    Examples:
      | id |
      | 10 |

  Scenario Outline: Update pet details
    When POST /pets
    And request-header Authenticate (string)
    And request-body (Pet)
    Then status 200

    Examples:
      | name   | type | status    | id | Authenticate  |
      | Archie | dog  | available | 10 | ($auth.token) |

  Scenario Outline: Delete an existing pet from the database
    When DELETE /pets/(id:number)
    And request-header Authenticate (string)
    Then status 200

    Examples:
      | id | Authenticate  |
      | 20 | ($auth.token) |

  Scenario Outline: Create a new pet
    And pattern Pet
      | name   | (string) |
      | type   | (string) |
      | status | (string) |
    When PUT /pets
    And request-header Authenticate (string)
    And request-body (Pet)
    Then status 200
    And response-body (number)

    Examples:
      | name  | type | status    | Authenticate  |
      | Socks | cat  | available | ($auth.token) |

  Scenario Outline: Search for pets
    When GET /pets?name=(string)&type=(string)&status=(string)
    Then status 200
    And response-body (Pets)

    Examples:
      | type | name      | status |
      | dog  |           |        |
      |      | available |        |
      |      |           | sold   |

  Scenario Outline: Place an order
    When POST /orders
    And request-header Authenticate (string)
    And request-body (Order)
    Then status 200

    Examples:
      | type | count | status  | id | Authenticate  |
      | dog  | 1     | pending | 30 | ($auth.token) |

  Scenario Outline: Get details of an order
    When GET /orders/order/(id:number)
    Then status 200
    And response-body (Order)

    Examples:
      | id |
      | 10 |

  Scenario Outline: Delete an order
    When DELETE /orders/order/(id:number)
    And request-header Authenticate (string)
    Then status 200

    Examples:
      | id | Authenticate  |
      | 20 | ($auth.token) |

  Scenario Outline: Update details of an order
    When POST /orders/order/(id:number)
    And request-header Authenticate (string)
    And request-body (string)
    Then status 200

    Examples:
      | type | count | status  | id | Authenticate  |
      | dog  | 1     | pending | 10 | ($auth.token) |

  Scenario Outline: Search for orders
    When GET /orders?type=(string)&status=(string)
    Then status 200
    And response-body (Orders)

    Examples:
      | type | status  |
      | dog  |         |
      |      | pending |

