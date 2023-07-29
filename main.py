# Name: Gliga Adrian Mircea
# Team: Wolfpack

# Final Project SDB
# (Asociatia TIPD)

# Organizer Menu Password: DPIT
# I made the QR Code Generator using this tutorial

from ui.console import participant_menu
from ui.console import organizer_menu

# The starting menu
while True:
    print("\nWelcome to ITPD!!!\n\n"
          "Choose your option:\n"
          "1.Enter as a Participant\n"
          "2.Enter as a Organizer\n"
          "3.Exit\n")
    try:
        command = int(input("Write the number here: "))
        if (command == 1):
            participant_menu()
        elif (command == 2):
            organizer_menu()
        elif (command == 3):
            break
    except:
        print("\nInvalid Command Try Again\n")
