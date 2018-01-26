import behave
from compare import expect

behave.use_step_matcher('re')



@given(u'I\'m in the option to create an account')
def step_impl(context):
    print("he")

@when(u'I introduce the following information')
def step_impl(context):
    print("good by")

@given(u'I have firt name (?P<first>[A-Za-z_]*)')
def step_impl(context, first):
    print(first)


@given(u'I have last name (?P<last>[A-Za-z_]*)')
def step_impl(context, last):
    print(last)

@given(u'I have username (?P<usname>[A-Za-z_0-9]*)')
def step_impl(context, usname):
    print(usname)



@given(u'I have password (?P<password>[A-Za-z_0-9*#@-]{8,16})')
def step_impl(context, password):
    #raise NotImplementedError(u'STEP: Given I have password passworD123')
    print(password)

@given(u'I have day (?P<day>[1-9]|[0-2][0-9]|31)')
def step_impl(context, day):
    print(day)

@given(u'I have month (?P<month>[1-9]|[0-1][0-2])')
def step_impl(context, month):
    print(month)

@given(u'I have year (?P<year>1[0-9]{3}|20[0-1][0-9])')
def step_impl(context, year):
    print(year)

@given(u'I have phone (?P<phone>[0-9]{7})')
def step_impl(context, phone):
    print(phone)
    expect(phone) == "4239868"


