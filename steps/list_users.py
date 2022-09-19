from behave import given, when
from models.list_users import ListUsers
from facts.list_user import ListUserFacts
from tasks.list_users import ListUserTask


@given("the user wants the information to appear in the '{param}'")
def given_I_am_the_tenant(context, param):
    context.data = ListUsers.from_file(param)

    status, header, body = ListUserFacts.get_list_user(param)
    context.status = status
    context.header = header
    context.body = body


@given("he extracts the object of id '{number}' from the '{data}' array of the response")
@when("he extracts the object of id '{number}' from the '{data}' array of the response")
def step_impl(context, number, data):
    list_users = context.data.__dict__
    context.current_object = ListUserTask.extract_object_by_id(int(number), context.body[data])
    context.expected_object = ListUserTask.extract_object_by_id(int(number), list_users[data])
    context.current_list_users_with_id_11 = ListUserTask.extract_object_by_id(int(number), context.body[data])
