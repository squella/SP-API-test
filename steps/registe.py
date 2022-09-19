from behave import given, when, then
from models.registe import RegisteUnsuccessfulRequest
from facts.register import RegisterUserFacts

@given("an user wants to register only an email '{email}'")
def given_I_am_the_tenant(context, email):
    context.register = RegisteUnsuccessfulRequest(email)
    

@when("user completed the registration process")
def step_impl(context):
    status, header, body = RegisterUserFacts.register(context.register)
    context.status = status
