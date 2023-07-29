# Name: Gliga Adrian Mircea
# Team: Wolfpack

# Final Project SDB
# (Asociatia TIPD)

# Organizer Menu Password: DPIT
# I made the QR Code Generator using this tutorial

from repository.repository import lists_of_events
from domain.event import Event
from datetime import datetime
from repository.repository import users
import qrcode

# Function for the organizer to add events
def add_event():
    try:
        new_event_id = int(len(lists_of_events) + 1)
        new_event_title = str(input("Give me the title of the Event: ")).capitalize()
        new_event_city = str(input("Give me the city of the Event: ")).capitalize()
        new_event_nr_participants = 0
        while True:
            new_event_max_places = int(input("Give me the maximum number of participants to the event: "))
            if (new_event_max_places > 0):
                break
        while True:
            new_event_starting_date = str(input("Give me the starting date of the event(dd/mm/yyyy): "))
            new_event_ending_date = str(input("Give me the ending date of the event(dd/mm/yyyy): "))
            new_event_starting_date_datetime = datetime.strptime(new_event_starting_date, "%d/%m/%Y")
            new_event_ending_date_datetime = datetime.strptime(new_event_ending_date, "%d/%m/%Y")
            if (new_event_starting_date_datetime < new_event_ending_date_datetime):
                break
            print("\n")
        new_event_website = str(input("Give me the event website"))

        print("\n")
        new_event_id = str(new_event_id) + "\n"
        new_event_title = str(new_event_title) + "\n"
        new_event_city = str(new_event_city) + "\n"
        new_event_nr_participants = str(new_event_nr_participants) + "\n"
        new_event_max_places = str(new_event_max_places) + "\n"
        new_event_starting_date = str(new_event_starting_date) + "\n"
        new_event_ending_date = str(new_event_ending_date) + "\n"
        new_event_website = str(new_event_website) + "\n"

        lists_of_events.append(
            Event(new_event_id, new_event_title, new_event_city, new_event_nr_participants, new_event_max_places,
                  new_event_starting_date, new_event_ending_date, new_event_website))

        w = open("events.txt", "w")

        for i in range(len(lists_of_events)):
            w.write("\n")
            w.write(str(lists_of_events[i].get_id()))
            w.write(str(lists_of_events[i].get_title()))
            w.write(str(lists_of_events[i].get_city()))
            w.write(str(lists_of_events[i].get_nr_participants()))
            w.write(str(lists_of_events[i].get_nr_max_places()))
            w.write(str(lists_of_events[i].get_starting_date()))
            w.write(str(lists_of_events[i].get_ending_date()))
            w.write(str(lists_of_events[i].get_website()))
        print("The event was added successfully!!!")
    except:
        print("ERROR")

# Function for the organizer to delete events
def delete_event():
    try:
        while True:
            given_id = int(input("Give me the ID from the event you want to delete: "))
            if (given_id > 0 and given_id <= len(lists_of_events)):
                break

        lists_of_events.pop(given_id - 1)
        i = given_id - 1
        while (i < len(lists_of_events)):
            old_event_id = lists_of_events[i].get_id()
            old_event_id = int(old_event_id)
            old_event_id -= 1
            old_event_id = str(old_event_id)
            old_event_id = old_event_id + "\n"
            lists_of_events[i].set_id(old_event_id)
            i += 1

        w = open("events.txt", "w")

        for i in range(len(lists_of_events)):
            w.write("\n")
            w.write(str(lists_of_events[i].get_id()))
            w.write(str(lists_of_events[i].get_title()))
            w.write(str(lists_of_events[i].get_city()))
            w.write(str(lists_of_events[i].get_nr_participants()))
            w.write(str(lists_of_events[i].get_nr_max_places()))
            w.write(str(lists_of_events[i].get_starting_date()))
            w.write(str(lists_of_events[i].get_ending_date()))
            w.write(str(lists_of_events[i].get_website()))

        print("The event was deleted successfully!!!")
    except:
        print("ERROR")

# Function for the organizer to delete events
def change_event():
    try:
        while True:
            given_id = int(input("Give me the ID from the event you want to change: "))
            if (given_id > 0 and given_id <= len(lists_of_events)):
                break
            print("\n")

        new_event_title = str(input("Give me the new title of the Event: ")).capitalize()
        new_event_city = str(input("Give me the new city of the Event: ")).capitalize()
        new_event_nr_max_places = int(input("Give me the new maximum number of participants to the event: "))
        while True:
            new_event_starting_date = str(input("Give me the new starting date of the event(dd/mm/yyyy): "))
            new_event_ending_date = str(input("Give me the new ending date of the event(dd/mm/yyyy): "))
            new_event_starting_date_datetime = datetime.strptime(new_event_starting_date, "%d/%m/%Y")
            new_event_ending_date_datetime = datetime.strptime(new_event_ending_date, "%d/%m/%Y")
            if (new_event_starting_date_datetime < new_event_ending_date_datetime):
                break
            print("\n")
        new_event_website = str(input("Give me the new website for the event: "))

        new_event_title = str(new_event_title) + "\n"
        new_event_city = str(new_event_city) + "\n"
        new_event_nr_max_places = str(new_event_nr_max_places) + "\n"
        new_event_starting_date = str(new_event_starting_date) + "\n"
        new_event_ending_date = str(new_event_ending_date) + "\n"
        new_event_website = str(new_event_website) + "\n"

        lists_of_events[given_id - 1].set_title(new_event_title)
        lists_of_events[given_id - 1].set_city(new_event_city)
        lists_of_events[given_id - 1].set_nr_max_places(new_event_nr_max_places)
        lists_of_events[given_id - 1].set_starting_date(new_event_starting_date)
        lists_of_events[given_id - 1].set_ending_date(new_event_ending_date)
        lists_of_events[given_id - 1].set_website(new_event_website)

        w = open("events.txt", "w")

        for i in range(len(lists_of_events)):
            w.write("\n")
            w.write(str(lists_of_events[i].get_id()))
            w.write(str(lists_of_events[i].get_title()))
            w.write(str(lists_of_events[i].get_city()))
            w.write(str(lists_of_events[i].get_nr_participants()))
            w.write(str(lists_of_events[i].get_nr_max_places()))
            w.write(str(lists_of_events[i].get_starting_date()))
            w.write(str(lists_of_events[i].get_ending_date()))
            w.write(str(lists_of_events[i].get_website()))
        print("The event was changed successfully!!!")
    except:
        print("ERROR")

# Function for the organizer to see the events in a specific city
def view_events_city():
    try:
        given_city = input("Give me the city: ")
        given_city = given_city.capitalize()
        given_city = given_city + "\n"
        for i in range(len(lists_of_events)):

            if given_city == lists_of_events[i].get_city():
                print(lists_of_events[i])

    except:
        print("Such city does not exist!")

# Function for the organizer to see the participants at a specific event
def view_participants():
    try:
        given_id = int(input("Enter Event ID: "))
        while True:
            if (given_id > 0 and given_id <= len(lists_of_events)):
                break
        print("\n")
        for i in range(len(users)):
            user_sign_up_list = users[i].get_sign_up_events()
            for j in range(len(user_sign_up_list)):
                if (int(user_sign_up_list[j]) == given_id):
                    print(users[i])
    except:
        print("ERROR")

# Function for the organizer to see events that have participants in descending order based on the number on participants
def view_events_descend_participants():
    lists_of_events_participants = []
    for i in range(len(lists_of_events)):
        if (int(lists_of_events[i].get_nr_participants()) != 0):
            lists_of_events_participants.append(lists_of_events[i])
    for i in range(len(lists_of_events_participants) - 1):
        for j in range(len(lists_of_events_participants)):
            if (lists_of_events_participants[i].get_nr_participants() > lists_of_events_participants[j].get_nr_participants()):
                change = lists_of_events_participants[i]
                lists_of_events_participants[i] = lists_of_events_participants[j]
                lists_of_events_participants[j] = change

    for i in range(len(lists_of_events_participants)):
        print(lists_of_events_participants[i])

# This function is for the organizer to generate QR Codes for events
# I made it using this tutorial: https://youtu.be/RsN0aXfPR1E
def create_qrcode():
    try:

        while True:
            given_id = int(input("Give me the ID of the event for which you want a QR code: "))
            if (given_id > 0 and given_id <= len(lists_of_events)):
                break

        features = qrcode.QRCode(version=1, box_size=40, border=3)
        features.add_data(lists_of_events[given_id].get_website())
        features.make(fit=True)
        generate_image = features.make_image(fill_color="black", back_color="white")
        generate_image.save("event_qr_code.png")

    except:
        print("ERROR")
