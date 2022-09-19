from behave import given, when
from models.single_user import SingletUsers
from facts.single_user import SingleUserFacts


@given("the user wants the information of the user with id '{param}'")
def given_I_am_the_tenant(context, param):
    context.data = SingletUsers.from_file(param)

    status, header, body = SingleUserFacts.get_single_user(param)
    context.status = status
    context.header = header
    context.body = body


@when("user extracts the '{data}' information")
def step_impl(context, data):
    current_information = context.data.__dict__
    context.current_object = context.body[data]
    context.expected_object = current_information[data]
    context.current_single_user = context.body[data]   
