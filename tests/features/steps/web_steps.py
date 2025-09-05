@then("I should see "{message}"")
def step_impl(context, message):
    """ Check the response message """
    assert message in str(context.resp.content)

@then("I should see "{name}"")
def step_impl(context, name):
    """ Check if product is found by name """
    found = False
    for product in context.data:
        if product["name"] == name:
            found = True
            break
    assert found is True

@then("I should not see "{name}"")
def step_impl(context, name):
    """ Check if product is not found by name """
    found = False
    for product in context.data:
        if product["name"] == name:
            found = True
            break
    assert found is False
