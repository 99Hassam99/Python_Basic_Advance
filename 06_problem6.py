# Can you change the self-parameter inside a class to something else (say
# “harry”) Try changing self to “slf” or “harry” and see the effects


import random
from random import randint


class train:
    def __init__(sllf,train_No):
        sllf.train_No=train_No # nothing will happen if we change the self parameter to slf

    def book_ticket(self,departure,arrival):
        print(f"Ticket is booked in train NO:{self.train_No} from {departure} to {arrival}")
    def get_status(self):
        print(f"Train NO:{self.train_No} is running successfully")

    def get_fare_info(self,departure,arrival):
        print(f"Ticket price in train NO:{self.train_No} from {departure} to {arrival} is {random.randint(4000,5000)}")

t=train(random.randint(1,100))
t.book_ticket("Peshawar","Karachi")
t.get_status()
t.get_fare_info("Peshawar","karachi")