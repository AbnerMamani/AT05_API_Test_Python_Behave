import behave
behave.use_step_matcher('re')


@given('I have {amount:d} bolivian in my account')
def step_impl(context, amount):
    #raise NotImplementedError(u'STEP: Given I have 100 bolivian in my account')
    print("Hello")

@given(u'I have a ZipCode as (?P<code>[0-9]*)')
def step_impl(context, code):
    #raise NotImplementedError(u'STEP: Given I have a ZipCode as 12154521')
    print(f"The code is {code} ")


@given(u'the country name is (?P<name>[A-Za-z_]*)')
def step_impl(context, name):
    #raise NotImplementedError(u'STEP: Given the country name is Canada')
    print("Name of the country:"+name)


@given(u'the number of habitants is (?P<habitants>[0-9]{1,3}|[0-9]{1,3}[\.][0-9]{3}|[0-9]{1,3}[\.][0-9]{3}[\.][0-9]{3})')
def step_impl(context, habitants):
    #raise NotImplementedError(u'STEP: Given the number of habitants is 123.110')
    print("Amount of that habitants")