from behave import given, when
from tasks.create_user import CreateUserTask
from models.create_user import CreateUserRequest


@given("an user with name '{Peter}' and job '{Sales}'")
def given_I_am_the_tenant(context, Peter, Sales):
    name = Peter
    job = Sales
    context.create_user = CreateUserRequest(name, job)

@when("the user is create with name and job as a parameters")
def step_impl(context):
   
    status, header, body = CreateUserTask.create_user(context.create_user)
    context.status = status
