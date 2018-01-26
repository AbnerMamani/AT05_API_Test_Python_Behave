# #from AbnerMamani.behave_customer.customer_search.dictionarys.Dictionary_users import Dictionary_users
#
if __name__ == '__main__':
     from behave_customer.customer_search.dictionarys.Dictionary_users import  Dictionary_users

import behave
from compare import expect
# from Dictionary_users import  Dictionary_users

dictionarys = Dictionary_users()

@given(u'I have a list clients with name')
def step_impl(context):
    global dictionarys
    context.dict_name = dictionarys.get_dictionary_by_name()



@given(u'I have a list clients wiht total price')
def step_impl(context):
    context.dict_price = dictionarys.get_dictionary_by_price()


@when(u'I enter the {name:w} to the client wiht his id is: {id:d} and price is: {price:d}')
def step_impl(context, name, id, price):
    context.name=name
    context.id=id
    context.price=price


@then(u'I verify that client with name is in the list')
def step_impl(context):
    currentKey=dictionarys.search_id_by_name(context.name, context.id)
    expect(context.dict_name[currentKey]) == context.name
    expect(context.dict_price[currentKey]) == context.price



@then(u'I verify that client with total priced is in the list')
def step_impl(context):
    currentKey=dictionarys.search_id_by_price(context.price, context.id)
    expect(context.dict_name[currentKey]) == context.name
    expect(context.dict_price[currentKey]) == context.price

