# Name: Gliga Adrian Mircea
# Team: Wolfpack

# Final Project SDB
# (Asociatia TIPD)

# Organizer Menu Password: DPIT
# I made the QR Code Generator using this tutorial

from repository.repository import lists_of_events
from datetime import datetime
from datetime import timedelta
from repository.repository import users
from domain.participant import Participant


# Function to show all the events
def view_all():
    for i in range(len(lists_of_events)):
        print(lists_of_events[i])


# Function for the user to sign up for any event
def join_event():
    try:
        given_name = str(input("Enter your name: "))
        safe_given_name = given_name
        does_user_already_exist = 0
        index_user = 0
        for i in range(len(users)):
            if (str(users[i].get_name()) == given_name):
                does_user_already_exist = 1
                index_user = i
                break
        if (does_user_already_exist == 1):
            try:
                while True:
                    given_id = int(input("Enter the ID of the Event you want to join: "))
                    if (given_id > 0 and given_id <= len(lists_of_events)):
                        break

                clone_of_list = users[index_user].get_sign_up_events()
                is_already=0
                for i in range(len(clone_of_list)):
                    if(given_id==int(clone_of_list[i])):
                        is_already=1
                if(is_already==1):
                    print("You are already sign up to this event!")
                else:
                    users[index_user].add_sign_up_events(given_id)
                    given_id -= 1
                    old_nr_participants = int(lists_of_events[given_id].get_nr_participants())
                    old_nr_participants += 1
                    old_nr_participants = str(old_nr_participants)
                    old_nr_participants = old_nr_participants + "\n"
                    lists_of_events[given_id].set_nr_participants(old_nr_participants)

                    w = open("events.txt", "w")

                    for j in range(len(lists_of_events)):
                        w.write("\n")
                        w.write(str(lists_of_events[j].get_id()))
                        w.write(str(lists_of_events[j].get_title()))
                        w.write(str(lists_of_events[j].get_city()))
                        w.write(str(lists_of_events[j].get_nr_participants()))
                        w.write(str(lists_of_events[j].get_nr_max_places()))
                        w.write(str(lists_of_events[j].get_starting_date()))
                        w.write(str(lists_of_events[j].get_ending_date()))
                        w.write(str(lists_of_events[j].get_website()))

                    print(f"Okay, you are sign up for {lists_of_events[given_id].get_title()}")
            except:
                print("ERROR")
        else:
            print("Welcome new user!")
            try:
                new_user_name = safe_given_name
                new_user_picture = str(input("Enter a link of a picture for your profile: "))
                while True:
                    given_id = int(input("Enter the ID of the Event you want to join: "))
                    if (given_id > 0 and given_id <= len(lists_of_events) - 1):
                        break
                users.append(Participant(new_user_name, new_user_picture, [given_id]))
                given_id -= 1
                old_nr_participants = int(lists_of_events[given_id].get_nr_participants())
                old_nr_participants += 1
                old_nr_participants = str(old_nr_participants)
                old_nr_participants = old_nr_participants + "\n"
                lists_of_events[given_id].set_nr_participants(old_nr_participants)
                w = open("events.txt", "w")

                for j in range(len(lists_of_events)):
                    w.write("\n")
                    w.write(str(lists_of_events[j].get_id()))
                    w.write(str(lists_of_events[j].get_title()))
                    w.write(str(lists_of_events[j].get_city()))
                    w.write(str(lists_of_events[j].get_nr_participants()))
                    w.write(str(lists_of_events[j].get_nr_max_places()))
                    w.write(str(lists_of_events[j].get_starting_date()))
                    w.write(str(lists_of_events[j].get_ending_date()))
                    w.write(str(lists_of_events[j].get_website()))
                print(f"Okay, you are sign up for {lists_of_events[given_id].get_title()}")
            except:
                print("Not a valid value!")
    except:
        print("ERROR")


# Function for the user to see the events that are going to take place in the next week in ascending order based
# on the number of maximum seats
def view_recent_events():
    one_week_future_date = datetime.now() + timedelta(days=7)
    events_in_one_week_list = []
    for i in range(len(lists_of_events)):
        date_of_event = datetime.strptime(lists_of_events[i].get_starting_date(), '%d/%m/%Y\n')
        if (date_of_event <= one_week_future_date):
            events_in_one_week_list.append(lists_of_events[i])

    for i in range(len(events_in_one_week_list) - 1):
        for j in range(len(events_in_one_week_list)):
            if (int(events_in_one_week_list[i].get_nr_max_places()) > int(events_in_one_week_list[
                                                                              j].get_nr_max_places())):
                change = events_in_one_week_list[i]
                events_in_one_week_list[i] = events_in_one_week_list[j]
                events_in_one_week_list[j] = change

    for i in range(len(events_in_one_week_list)):
        print(events_in_one_week_list[i])

# Function for the user to see the events in the month that he wants in descending order based on duration
def view_events_by_month():
    try:
        while True:
            given_month = int(input("Give me the month(in number): "))
            if (given_month >= 1 and given_month <= 12):
                break
        lists_of_events_given_month = []

        for i in range(len(lists_of_events)):
            event_starting_date = datetime.strptime(lists_of_events[i].get_starting_date(), '%d/%m/%Y\n')
            if (given_month == event_starting_date.month):
                lists_of_events_given_month.append(lists_of_events[i])
        for i in range(len(lists_of_events_given_month) - 1):
            for j in range(len(lists_of_events_given_month)):
                first_event_starting = datetime.strptime(lists_of_events[i].get_starting_date(),
                                                         '%d/%m/%Y\n')
                first_event_ending = datetime.strptime(lists_of_events[i].get_ending_date(), '%d/%m/%Y\n')
                first_event_duration = first_event_ending - first_event_starting
                second_event_starting = datetime.strptime(lists_of_events[j].get_starting_date(),
                                                          '%d/%m/%Y\n')
                second_event_ending = datetime.strptime(lists_of_events[j].get_ending_date(), '%d/%m/%Y\n')
                second_event_duration = second_event_ending - second_event_starting
                if (first_event_duration > second_event_duration):
                    change = lists_of_events_given_month[i]
                    lists_of_events_given_month[i] = lists_of_events_given_month[j]
                    lists_of_events_given_month[j] = change

        for i in range(len(lists_of_events_given_month)):
            print(lists_of_events_given_month[i])
            print(lists_of_events[i].get_duration())
            print("\n")
    except:
        print("Such month does not exist!")
