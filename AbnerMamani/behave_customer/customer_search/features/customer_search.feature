Feature: Customer search

Scenario Outline: Search a client by total price of a list clients
   Given I have a list clients with name
        and I have a list clients wiht total price
   When I enter the <Name> to the client wiht his id is: <Id> and price is: <Price>
   Then I verify that client with total priced is in the list
   Examples:
	| Name      | Id | Price |
	| Carlos    | 1  | 50    |
	| Pinocho   | 2  | 100   |
    | Julia     | 3  | 200   |


Scenario: Search a client by name of a list clients
   Given I have a list clients with name
        and I have a list clients wiht total price
   When I enter the Carlos to the client wiht his id is: 1 and price is: 50
   Then I verify that client with name is in the list


