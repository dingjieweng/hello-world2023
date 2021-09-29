# DEEP DEEP FOREST
# Now updated to Python 3

# At the top of the file are declarations and variables we need.
# 
# Scroll to the bottom and look for the main() function, that is
# where the program logic starts.

import random # random numbers (https://docs.python.org/3.3/library/random.html)
import sys # system stuff for exiting (https://docs.python.org/3/library/sys.html)


player = { 
    "name": "p1", 
    "score": 0,
    "items" : ["milk"],
    "friends" : [],
    "location" : "start"}

rooms = {
    "room1" : "bedroom",
    "room2" : "stairs",
    "room3" : "deadroom" }




def printGraphic(name):
    if (name == "fox"):
        print ('   /\   /\            ')
        print ('  // \_// \     ____  ')
        print ('  \_     _/    /   /  ')
        print ('   / * * \    /^^^]   ')
        print ('   \_\O/_/    [   ]   ')
        print ('    /   \_    [   /   ')
        print ('    \     \_  /  /    ')
        print ('     [ [ /  \/ _/     ')
        print ('    _[ [ \  /_/       ')
        print ('                      ')
        print ('       the fox        ')

   # The graphic of the key.     
    if ( name == "key"):
       print ('    __')
       print ('   / o')
       print ('   \_ /')
       print ('    <|')
       print ('    <|')
       print ('    <|')
     
def happyEnd():
    print("")
    print("You put the key inside the lock.")
    print("You turned it. It worked")
    print("You opened the door.")
    print("CONGRATULATIONS! YOU WIN!")




# The room you escaped successfully. You made the right choice.

def exitRoom():
    print(" ")    
    print("You kept walking. You saw there's door on the left side.")
    print("Your options: [ yes , no ]")
   
    pcmd = input("Do you wanna turn left? >")
    if (pcmd == "yes"):
        print ("You took a left turn. Sprinted to the door. ")
        print ("You could hear someone's behind you. It's getting closer. ")
        print ("You grab the door knob. Turned it.")
        print ("It's locked!")

    # check the list for items
    # the 'in' keyword helps us do this easily
    if ("key" in player["items"]):
         print ("options: [ use the key , bang the door , run  ]")
    else:
         print ("options: [ bang the door , run  ]")

    pcmd = input(">")

    # option 1: bang the door
    if (pcmd == "bang the door"):
        print ("You bang the door... It doesn't help.")
        deadRoom() # Dead
    
    # option 2: run
    elif (pcmd == "run"):
        print ("You try to run but there's no way to run!")
        deadRoom()

    # option 3: use the key
    elif (pcmd == "use the key"):
        print ("You use the key to open the door!")
        input("press enter>")
        printGraphic("key")
        happyEnd()
   
    else:
        print ("No? ...Okay .")
        pcmd = input("press enter >")
        deadRoom() # deadEnd.


# The room you died. You made the wrong choice.
def deadRoom():

    print(" ")
    print("You suddenly feel strong pain on your back.")
    print("You were injured! You were bleeding! ")
    print("You lost consciousness.")
    print("YOU DIED! BAD END.")


# an object describing our player
# This is where you found the key!
def stairs():
    print("You slowly walked down stairs.")
    print("You saw there's a key on the nearest table.")
    printGraphic("key")

    print ("Do you wanna grab it?")
    print ("Your options: [ yes , no ]")
    pcmd = input("type yes or no >")

    # the player can choose yes or no
    if (pcmd == "no"):
        print ("You left the key on the table.")
        input("press enter >")
        deadRoom()
    elif (pcmd == "yes"):
        print ("You took the key, Put it into your pocket...")    
        player["items"].append("key") # add an item to the array with append

        exitRoom()
    
    
    
    
    else:
        print ("No? ...Okay .")
        pcmd = input("press enter >")
        deadRoom() # deadEnd.


def bedroom():
    print ("You are standing in the bedroom you woke up. ")
    print ("There's a door right in front of you. ")
    
    # this piece of game logic checks to see if the requirements are met to continue.
    # we can have some fun and change the options for the player
    # based on variables we stored

    # 1. check the list of items, to see if it is there
    # 2. check the list of friends, to see if you are in friends list

   
    print ("Your options: [ open the door , exit ]")

    pcmd = input(">") # user input

    # player options
    if (pcmd == "open the door"):
        # its a trick!
        print ("You opened the door... now you can see there are stairs going down. ")

        input("press enter >")
        stairs()

   

    else:
        print ("I don't understand that")
        bedroom() # the beginning

def introStory():
    # let's introduce them to our world
    print ("Good evening! What's your name?")
    player["name"] = input("Please enter your name >")

    # intro story, quick and dirty (think star wars style)
    print("-----------------------------")
    print ("Welcome to Escape the Night!")
    print ("Try to stay alive..." + player["name"]+".")
    print ("      ")
    print ("The story became...")
    print ("You woke up. You realized you're in a strange place.")
    print ("This is not your house. You couldn't recall how you got here.")
    print ("Do you wanna get up?")

    pcmd = input("please choose yes or no >")

    # the player can choose yes or no
    if (pcmd == "yes"):
        print ("You got up from the bed, You look around...")
        input("press enter >")
        bedroom()
    else:
        print ("No? ... You lied back on the bed. Wondering how you got here.")
        pcmd = input("press enter >")
        introStory() # repeat over and over until the player chooses yes!



# main! most programs start with this.
def main():
    printGraphic("title") # call the function to print an image
    introStory() # start the intro

main() # this is the first thing that happens