Feature: Get list users
    As a public API consumer,
    I want to test my front-end against a real API,
    So that I can retrieve their attributes details,
    and they start appearing on my searches/recommendations results.


    Scenario: Add a batch that contains new products
        Given I am the tenant
        When I add the products
        Then the products registration is accepted