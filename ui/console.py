# Name: Gliga Adrian Mircea
# Team: Wolfpack

# Final Project SDB
# (Asociatia TIPD)

# Organizer Menu Password: DPIT
# I made the QR Code Generator using this tutorial

from service.participant_service import view_all, join_event, view_recent_events, view_events_by_month
from service.organizer_service import add_event, delete_event, change_event, view_events_city, \
    view_events_descend_participants, view_participants, create_qrcode

# The menu for any one who wants to participate
def participant_menu():
    while True:
        print("\nWelcome Participant\n\n"
              "Choose your option:\n"
              "1.View all events\n"
              "2.Join an Event\n"
              "3.View events that are in the next 7 days in ascending order according to the maximum number of seats\n"
              "4.View events that starts in the month that you want(showed in descending order based on duration)\n"
              "5.Go Back\n")
        try:
            command = int(input("Write the number here: "))
            if (command == 1):
                view_all()
            elif (command == 2):
                join_event()
            elif (command == 3):
                view_recent_events()
            elif (command == 4):
                view_events_by_month()
            elif (command == 5):
                break
        except:
            print("\nInvalid Command Try Again\n")


# Password: DPIT
# The menu only for the organizers(availebel only with password)
def organizer_menu():
    while True:
        password = input("\nEnter the password: ")
        if(password == "DPIT"):
            break
    while True:

        print("\nWelcome Organizer\n\n"
              "Choose your option:\n"
              "1.Add an Event\n"
              "2.Delete an Event(identified by id)\n"
              "3.Change the info for an Event(identified by id)\n"
              "4.View all Events\n"
              "5.View the Events from a city(given by you)\n"
              "6.View the participants from an Event(identified by id)\n"
              "7.View the events in descending order based on the number of participants(just the one that have participants)\n"
              "8.Generate QR Code\n"
              "9.Go Back\n")
        try:
            command = int(input("Write the number here: "))
            if (command == 1):
                add_event()
            elif (command == 2):
                delete_event()
            elif (command == 3):
                change_event()
            elif (command == 4):
                view_all()
            elif (command == 5):
                view_events_city()
            elif (command == 6):
                view_participants()
            elif (command == 7):
                view_events_descend_participants()
            elif (command == 8):
                # I made it using this tutorial: https://youtu.be/RsN0aXfPR1E
                create_qrcode()
            elif (command == 9):
                break
        except:
            print("\nInvalid Command Try Again\n")