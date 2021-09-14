from utils import bands_module_text_files

"""
This program consists of a main file (this file) that interacts with another file that is the interface
for the program.The program begins by going through all the functions on this page and then recognises that 
menu() is called. 
The menu() function consists of the main loop/user direction for the program. While the user does not hit 'q' 
do the following.

If the user enters 'a':
The function add_band() is called. This function asks the user fo some input then stores the information in 
variables and then passes those variables to the band_info() function in the module file called bands_module_text_files. 
In the band_info() function in the bands_module_text_files the three parameters are taken in. 
The 'bands_info.txt' is opened in append mode. The information is written to the file in the form of a formatted string
and the information is appended to the end of the file using 'a' mode instead of using 'w' mode which would completely 
re-write the entire file.

If the user enters 'l':
The function show_band() is called. The list_band_info() function in the bands_module_text_files is accessed and 
stored in the variable bands. 
In the list_band_info() function the band_info.txt file is opened in "r" mode.
A variable called lines is created to store a list comprehension that is used to to strip the space at the end 
of each line and each word is split at the comma.
A list containing a dictionary is created to assign each key to a certain part of the list. This list is then returned.
Back in the show_band() function on this page I iterate over the list_band_info() function and assign each key 
in list_band_info() function to the iterable (band) for example band['producer']. This statement is
printed out as a formatted string to the console.
I have also included a try/except to handle a FileNotFoundError which occurs if I run the program and try to list 
the bands without adding any information.

If the user enters 'm':
The function heard_album() is called. In this function the user is asked to enter an album and this variable gets 
passed to the listened_to_album_info() in the bands_module_text_files and takes in the user input as a parameter.
I iterate over list_band_info() and if an index of band['name'] is the same as what the user entered then 
band['listened to: '] is changed to yes.


If the user enters 'd':
The function delete_band() is called. In this function the user is asked to enter a band to delete and this variable 
gets passed to the delete_band_info() in the bands_module_text_files and takes in the user input as a parameter.
In the delete_band_info() function a new list is created containing every dictionary entered except what the user 
entered. The _save_all_info() is called and the variable the stores the new list is passed as an argument and the 
information is updated.

"""
USER_INPUT = """
------------------------------------------------------------------------
Enter:
- 'a' to add a new band
- 'l' to list all the bands
- 'm' to mark an album as listened to
- 'd' to delete a band and it's info
- 'q' to quit the program
: 
------------------------------------------------------------------------
"""


# --------------------------------------------------START OF FUNCTIONS--------------------------------------------------
def menu():
    user_input = input(USER_INPUT).lower()
    while user_input != 'q':
        if user_input == 'a':
            add_band()

        elif user_input == 'l':
            try:
                show_band()
            except FileNotFoundError:
                print("Empty file try adding some bands")

        elif user_input == 'm':
            heard_album()

        elif user_input == 'd':
            delete_band()
        else:

            print("Not valid try again")
        user_input = input(USER_INPUT).lower()


def add_band():
    band = input("Enter a band ")
    album = input("Enter an album ")
    producer = input("Enter a producer ")

    bands_module_text_files.band_info(band, album, producer)


def show_band():
    bands = bands_module_text_files.list_band_info()
    for band in bands:
        print(
            f"Band: {band['name']},Album: {band['album']},"
            f"Producer: {band['producer']},listened to: {band['listened to: ']}")


def heard_album():
    user_album = input("Enter an album to mark as listened to ")
    bands_module_text_files.listened_to_album_info(user_album)


def delete_band():
    band = input("Enter a band to delete ")
    bands_module_text_files.delete_band_info(band)


# --------------------------------------------------END OF FUNCTIONS----------------------------------------------------
menu()
