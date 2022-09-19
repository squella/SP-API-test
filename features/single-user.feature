Feature: Get single user
    
    @test_02
    Scenario: Get a single user
        Given the user wants the information of the user with id '11'
        When user extracts the 'data' information
        Then the response body is as expected
        And the request succeeded
