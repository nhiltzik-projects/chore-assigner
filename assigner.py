from datetime import datetime
from datetime import date
#print(datetime.date(datetime.now()))

REF_DATE = date(2020,2,14)

def weeks_between(today):
    return round(abs((today-REF_DATE).days/7))

def assign_task(week_number):
    tasks = ["Kitchen", "Garbage", "Living Room", "Hallway"]

    #phone_dictionary = {"Sruli":123, "Alex":123, "Noam":123, "Ariel":123}

    #roommates_permutations = [["Sruli", "Alex", "Noam", "Ariel"],
    #           ["Alex", "Noam", "Ariel", "Sruli"],
    #           ["Noam", "Ariel", "Sruli", "Alex"], 
    #           ["Ariel", "Sruli", "Alex", "Noam"]]

    

    this_week = roommates_permutations[week_number % 4]
    return dict(zip(this_week, tasks))




    



def main():
    today = datetime.date(datetime.now())
    print(weeks_between(today))

main()