Feature: User data comparison

    @test_05
    Scenario: Data extracted from list of users is the same as the data returned from the single user
        Given the user wants the information to appear in the 'page=2'
        And he extracts the object of id '11' from the 'data' array of the response
        And the user wants the information of the user with id '11'
        When user extracts the 'data' information
        Then list of users information is the same as the single user data
