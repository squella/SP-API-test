Feature: Get list users

    @test_01
    Scenario: Get a list of users
        Given the user wants the information to appear in the 'page=2'
        When he extracts the object of id '11' from the 'data' array of the response
        Then the request succeeded
        And the response body is as expected

