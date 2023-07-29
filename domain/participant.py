# Name: Gliga Adrian Mircea
# Team: Wolfpack

# Final Project SDB
# (Asociatia TIPD)

# Organizer Menu Password: DPIT
# I made the QR Code Generator using this tutorial

class Participant:
    def __init__(self, name, picture, sing_up_events):
        self.__name = name
        self.__picture = picture
        self.__sign_up_events = sing_up_events

    # This function gets the name of the participant
    def get_name(self):
        return self.__name

     # This function sets the name of the prticipant
    def set_name(self, new_name):
        self.__name = new_name

    # This function gets the link to the profile picture that the user has
    def get_picture(self):
        return self.__picture

    # This function sets the link to the profile picture that the user has
    def set_picture(self, new_picture):
        self.__picture = new_picture

    # This function gets the list of the IDs of the events that the participant is sign up to
    def get_sign_up_events(self):
        return self.__sign_up_events

    # This function adds the ID of the event that the user sign up to
    def add_sign_up_events(self, new_event_id):
        self.__sign_up_events.append(new_event_id)

    # This function gets the length of the list
    def get_sign_up_events_list_lenght(self):
        return len(self.__sign_up_events)

    # This function writes the info for the participant
    def __str__(self):
        return f"Name: {self.__name}, \n Picture Link: {self.__picture},\n Sign Up Events {self.__sign_up_events}"

    # This function helps the function on line 45
    def __repr__(self):
        return str(self)

    # This function verifies if two participants are the same
    def __eq__(self, other):
        return self.get_name() == other.get_name()
