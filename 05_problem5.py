# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.
import random
from random import randint


class train:
    def __init__(self,train_No):
        self.train_No=train_No

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