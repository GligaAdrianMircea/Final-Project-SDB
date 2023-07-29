# Name: Gliga Adrian Mircea
# Team: Wolfpack

# Final Project SDB
# (Asociatia TIPD)

# Organizer Menu Password: DPIT
# I made the QR Code Generator using this tutorial

from datetime import datetime

# This is the entity for an event
class Event:
    def __init__(self, id, title, city, nr_participants, nr_max_places, starting_date, ending_date, website):
        self.__id = id
        self.__title = title
        self.__city = city
        self.__nr_participants = nr_participants
        self.__nr_max_places = nr_max_places
        self.__starting_date = starting_date
        self.__ending_date = ending_date
        self.__website = website

    # This function gets the ID for the event
    def get_id(self):
        return self.__id

    # This function sets the ID for the event
    def set_id(self, new_id):
        self.__id = new_id

    # This function gets the title for the event
    def get_title(self):
        return self.__title

    # This function sets the title for the event
    def set_title(self, new_title):
        self.__title = new_title

    # This function gets the city for the event
    def get_city(self):
        return self.__city

    # This function sets the city for the event
    def set_city(self, new_city):
        self.__city = new_city

    # This function gets the number of participants for the event
    def get_nr_participants(self):
        return self.__nr_participants

    # This function sets the number of participants for the event
    def set_nr_participants(self, new_nr_participants):
        self.__nr_participants = new_nr_participants

    # This function gets the maximum number of seats for the event
    def get_nr_max_places(self):
        return self.__nr_max_places

    # This function sets the maximum number of seats for the event
    def set_nr_max_places(self, new_nr_max_places):
        self.__nr_max_places = new_nr_max_places

    # This function gets the starting date of the event
    def get_starting_date(self):
        return self.__starting_date

    # This function sets the starting date for the event
    def set_starting_date(self, new_starting_date):
        self.__starting_date = new_starting_date

    # This function gets the ending date of the event
    def get_ending_date(self):
        return self.__ending_date

    # This function sets the ending date for the event
    def set_ending_date(self, new_ending_date):
        self.__ending_date = new_ending_date

    # This function gets the duration of the event
    def get_duration(self):
        local_starting_date = datetime.strptime(self.get_starting_date(), "%d/%m/%Y\n")
        local_ending_date = datetime.strptime(self.get_ending_date(), "%d/%m/%Y\n")
        event_duration = local_ending_date - local_starting_date
        return event_duration

    # This function gets the website for the event
    def get_website(self):
        return self.__website

    # This function sets the website for the event
    def set_website(self, new_website):
        self.__website = new_website

    # This function writes the info for the event
    def __str__(self):
        return f"{self.__id} Title: {self.__title} City: {self.__city} Nr. Participants: {self.__nr_participants} Max Seats: {self.__nr_max_places} Starting Date: {self.__starting_date} Ending Date: {self.__ending_date} Website: {self.__website}"

    # This function helps the function on line 45
    def __repr__(self):
        return str(self)

    # This function verifies if two events are the same
    def __eq__(self, other):
        return self.get_title() == other.get_title()
