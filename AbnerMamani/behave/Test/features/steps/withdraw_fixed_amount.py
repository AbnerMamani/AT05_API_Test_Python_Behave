from compare import expect


@given(u'I have ${balance} in my account')
def step_impl(context, balance):
    context.balnce=int(balance)

@when(u'I choose to withdraw the fixed amount of ${withdraw}')
def step_impl(context, withdraw):
    context.withdraw = int(withdraw)

@then(u'I should receive ${cash} cash')
def step_impl(context, cash):
    print("This is your"+cash)

@then(u'the balance of my account should be ${balnce}')
def step_impl(context, balnce):
    resul=context.balnce - context.withdraw
    expect(balnce) == str(resul)