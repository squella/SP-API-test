Feature: Create user
    
    @test_03
    Scenario: register user
        Given an user with name 'Peter' and job 'Sales'
        When the user is create with name and job as a parameters
        Then the new user was created