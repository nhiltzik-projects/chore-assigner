from datetime import datetime
from datetime import date
import numpy as np
#print(datetime.date(datetime.now()))

REF_DATE = date(2020,2,7)

def weeks_between(today):
    return round(abs((today-REF_DATE).days/7))

def assign_task(week_number):
    #assigns chores to each roommate based on week

    # chores
    tasks = ["Kitchen", "Garbage", "Living Room", "Hallway"]

    #list of roommates
    roommate_array = np.array(["Sruli", "Alex", "Noam", "Ariel"])

    #shuffles roomates per week in the cycle
    shuffled_roommates = np.roll(roommate_array, week_number % 4)

    return dict(zip(list(shuffled_roommates), tasks))


def main():
    today = datetime.date(datetime.now())
    
    week_number = weeks_between(today)

    print(assign_task(week_number))

    

main()