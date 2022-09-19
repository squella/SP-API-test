Feature: user registration

    @test_04
    Scenario: register user without password
        Given an user wants to register only an email 'sydney@fif'
        When user completed the registration process
        Then the user registration is not processed