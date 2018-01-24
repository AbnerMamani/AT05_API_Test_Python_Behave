from SMS_store import SMS_store
my_sms=SMS_store()


def load_sms():
    """
    Function that load the values to inbox
    :return: nome
    """
    global my_sms
    my_sms.add_new_arrival("71342516", "2018-01-23 11:15:09.20", "Text of the SMS 1")
    my_sms.add_new_arrival("71342517", "2018-01-23 12:15:09.20", "Text of the SMS 2")
    my_sms.add_new_arrival("71342518", "2018-01-23 13:15:09.20", "Text of the SMS 3")
    my_sms.add_new_arrival("71342519", "2018-01-23 14:15:09.20", "Text of the SMS 4")
    my_sms.add_new_arrival("71342506", "2018-01-23 15:15:09.20", "Text of the SMS 5")
    my_sms.add_new_arrival("71342516", "2018-01-23 16:15:09.20", "Text of the SMS 6")
    my_sms.add_new_arrival("71342526", "2018-01-23 17:15:09.20", "Text of the SMS 7")

#Use class and functions 
def showTupla(li):
    for a in li:
        print(a)

load_sms()
print("List of the inbox")
showTupla(my_sms.inbox)
print(f"\n Number of sms messages in inbox is: {my_sms.message_count()}")
print(f"\n The message number 2 is: {my_sms.get_message(2)}")
print("\n List of unread sms is")
showTupla(my_sms.get_unread_indexes())

print("\n List after deleting the SMS 3 is")
my_sms.delete(3)
showTupla(my_sms.inbox)

print("\n list after clear the SMS inbox is ")
my_sms.clear()
showTupla(my_sms.inbox)
