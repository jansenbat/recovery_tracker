"""
Premise: keep track of my injured arm and how I'm coming along with it
"""

def add():
    date = input("What is the date for this entry? mm/dd/yy: ")
    obs_type = input("What kind of observation are you logging? ")   # is the observation one with strength, coordination, etc.
    observation = input("What observations would you like to note? ")   # just write any observations you would like to note
    pain_level = input("Expereince any pain? If so enter a number between 1 and 10: ")

    with open('recovery_diary.txt', 'a') as j:
        j.write(date + " | " + obs_type + " | " + observation + " | " + pain_level + "\n")


def view():
    with open('recovery_diary.txt', 'r') as jj:
        for log in jj.readlines():
            logs = log.rstrip()
            datee, type, obss, painn = logs.split(" | ")
            print("Date: " + datee + ", Observation Type: " + type + ", Observation Note(s): " + obss + ", Pain Level: " + painn)


while True:
    request = input("What would you like to do? Add(a), View(v), Quit(q)? ").lower()
    if request == "q":
        print("Thank you for using our service, come again!")
        break
    elif request == "a":
        add()
    elif request == "v":
        view()
    else:
        print("Invalid input.")
        continue
