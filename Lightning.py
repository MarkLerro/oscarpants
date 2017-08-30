#!/usr/bin/python


"""This is a program to create a "set list" of music for a band with a defined
length of time. The initial arguments to be enetered from the command line are
the "Venue name" and the "date of show".These will also serve to be the name of
the file saved at the end of the program.
The menu list will offer options to Create a set list, add or remove songs, and
print out list while saving as a txt file.


"""
#Import sys Module
import sys


#Create Class
class Songs():
    def __init__(self, songnames_list):
        self.songnames = songnames_list
        
    def print_menu(self):
        """ Prints out the user options """
       
        print('1. Enter set length in min (no seconds)')
        print('2. add new song to list')
        print('3. Lookup a song name')
        print('4. Remove song from list')
        print('5. Print avaiable songs Save and Quit')
        print()  
 #Function to create set list and length of set
    def list_create(self, set_len):
        titles=[]
        total_setime = 0
        for title,song_len in self.songnames.items():
            titles.append(title)
            total_setime = total_setime + song_len
            if total_setime >= set_len:
                return titles, total_setime
        else:
            print ('Set length is less than requested', set_len)
            return titles, total_setime
#Function to print songs
    def show_lib(self):
        for title in self.songnames.keys():
            print (title)

# Create dictionary with key = Names, value = song._name

songnames = dict()
songnames['Moles Theme'] = 4
songnames['Picture Book'] = 3
songnames['The Man'] = 3
songnames['Say Anything'] = 4
songnames['Said'] = 5
songnames['Alcohol'] = 8
songnames['Wrong Place'] = 9
songnames['Bad Sighn'] = 6
songnames['Mary Ann'] = 6
songnames['Darkness on the Delta'] = 5

songs = Songs(songnames)  # create an instance of the class

# setup counter to store menu choice
menu_choice = 0
set_length = 0

# Get venue name and date from cmd line args
if len(sys.argv) > 1:
#    print('argv')
#    print (sys.argv)
    venue_name = sys.argv[1]
    venue_date = sys.argv[2]
else:
    venue_name = 'ThePlace'
    venue_date = '2017-10-02'
print ('Venue name', venue_name, ' Date:', venue_date)

# as long as the menu choice isn't "quit" get user options
while menu_choice != 5:
# display your menu    
    songs.print_menu()
    
    
    # get menu choice from user
    try:
        menu_choice = int(input("Type in a number (1-5): "))
    except:
        print('Please enter a valid integer')
        continue

    
    # view current entries
    if menu_choice == 1:
        try:
            print ("Length of set in Min:")
            set_len = int(input("type number of Minutes"))
            print ("set Len as entered", set_len)
        except:
            print('Please try again')
            continue


        # Creating the playlist 
        
  # Perform a calculation on a list
        set_list, set_length = songs.list_create(set_len)  
        print (set_list)
        print ('This set has', len(set_list), 'songs in it')
        print ("this set is", set_length, "Minutes Long")


    # add an entry
    elif menu_choice == 2:
        print("Add Song")
        try:
            songname = input("Song Name: ")
            song_len = int(input("Song Length (min): "))
            songnames[songname]=song_len
            songs.show_lib()
        except:
            print('Please try again')
            continue

            # remove an entry
    elif menu_choice == 4:
        print("Remove Song")
        name = input("Name: ")
        try:
            if name in songnames:
                del (songnames[name])
        except:
            print('Please try again')
            continue

    # view user name
    elif menu_choice == 3:
        print("Lookup Song.")
        try:
            name = input("Name: ")
            if name in songnames:
                print("Name: {} \tSong Length: {} \n".format(name, songnames[name]))
            else:
                print("songname not found")
        except:
            print('Please try again')
            continue

    # is user enters something strange, show them the menu
    elif menu_choice != 5:
         songs.print_menu()
    elif menu_choice == 5:
        print("Avaiable Songs")
        songs.show_lib()
        filename = venue_name + '_' + venue_date +'.txt'
        file = open(filename,"w")
        file.write(venue_name + "\n")
        file.write(venue_date + "\n")
        for title in songnames.keys():
            file.write(title + "\n")
        file.write("set List" + str(set_list) + "\n")
        file.write( "set Length" + str( set_length ) + "\n" )
        file.close()
        print ('Wrote to file:', filename)
