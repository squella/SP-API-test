from behave import then


@then("list of users information is the same as the single user data")
def step_impl(context):
    assert context.current_single_user == context.current_list_users_with_id_11
