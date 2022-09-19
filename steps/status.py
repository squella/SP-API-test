from behave import then
from questions.status import StatusQuestions

@then("the request succeeded")
def step_impl(context):    
    assert(StatusQuestions.is_ok(context.status))
    
@then("the new user was created")
def step_impl(context):    
    assert(StatusQuestions.is_created(context.status))

@then("the user registration is not processed")
def step_impl(context):    
    assert(StatusQuestions.has_syntactic_error(context.status))