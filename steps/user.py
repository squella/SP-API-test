from behave import given, when, then


@given("I am the tenant")
def given_I_am_the_tenant(context):
    print("hellow world")

@when(u'I add the products')
def step_impl(context):
    print("hellow world")


@then(u'the products registration is accepted')
def step_impl(context):
    print("hellow world")