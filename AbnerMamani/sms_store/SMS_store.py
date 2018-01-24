class SMS_store:
   """
   Class that instantiate SMS_store objects,
   """
   def __init__(self):
       self.inbox = []

   def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
       """
        Makes new SMS tuple, inserts it after other messages
        in the store. When creating this message, its # has_been_viewed status is set False.
       """
       has_been_viewed = False
       self.inbox.append((has_been_viewed, from_number, time_arrived, text_of_SMS))

   def message_count(self):
       """
       Returns the number of sms messages in my_inbox
       :return: inbox length
       """
       return len(self.inbox)

   def get_unread_indexes(self):
       """
       Returns list of indexes of all not-yet-viewed SMS messages
       :return: list of all not-yet-viewed SMS messages
       """
       underead = []
       for sms in self.inbox:
           if not sms[0]:
               underead.append(sms)
       return underead

   def get_message(self, i):
       """
       Return (from_number, time_arrived, text_of_sms) for message[i]
       :param i: index of the list
       :return: (from_number, time_arrived, text_of_sms)
       """
       if i< self.message_count():
           sms = self.inbox[i]
           sms = (True,) + sms[1:]
           self.inbox[i] = sms
           return self.inbox[i][1:]
       return "None"

   def delete(self, i):
    """
    Delete the message at index i 
    :param i: index
    :return: None
    """""
    self.inbox.pop(i)

   def clear(self):
       """
       Delete all messages from inbox
       :return: Nome
       """
       self.inbox = []

