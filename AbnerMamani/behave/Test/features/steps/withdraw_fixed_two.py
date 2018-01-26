import parse
from behave import register_type, given


@parse.with_pattern(r'[\w\d.-]+@[\w.-]+')
def parse_email(text):
   return text

register_type(Email=parse_email)


@given(u'I have email {emails:Email}')
def step_impl(context, emails):
    print("sx")