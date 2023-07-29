# Name: Gliga Adrian Mircea
# Team: Wolfpack

# Final Project SDB
# (Asociatia TIPD)

# Organizer Menu Password: DPIT
# I made the QR Code Generator using this tutorial

from domain.event import Event
from domain.participant import Participant

# This part is to read the events from a file and add it to a list
f = open("events.txt", "r")
lists_of_events = []

for i in f:
    event_id = str(f.readline())
    event_title = str(f.readline())
    event_city = str(f.readline())
    event_nr_participants = str(f.readline())
    event_max_places = str(f.readline())
    event_starting_date = str(f.readline())
    event_ending_date = str(f.readline())
    event_website = str(f.readline())

    lists_of_events.append(Event(event_id, event_title, event_city, event_nr_participants, event_max_places,
                                 event_starting_date, event_ending_date, event_website))

# This is a hard coded list of users
users = [Participant("Alex Smith", "https://unsplash.com/photos/ILip77SbmOE", [1, 2, 5]),
         Participant("John Robinson", "https://unsplash.com/photos/man-standing-near-balcony-5aGUyCW_PJw", [1, 3]),
         Participant("Ivy Williams", "https://unsplash.com/photos/QXevDflbl8A", [1, 2]),
         Participant("Willow Baker", "https://unsplash.com/photos/a-woman-covers-her-face-with-her-hands-oz9fHNCUhZc",
                     [], ),
         Participant("Jack West", "https://unsplash.com/photos/X6Uj51n5CE8", [1,2,3,4,5]),
         Participant("Mason Dixon", "https://unsplash.com/photos/iFgRcqHznqg", [4,5]),
         Participant("Riley Yates",
                     "https://unsplash.com/photos/portrait-of-a-nonbinary-autistic-person-outdoors-using-headphones-dotm8dUpAxc",
                     []),
         Participant("Lincoln Cooke", "https://unsplash.com/photos/rDEOVtE7vOs", [1,4,5]), ]
