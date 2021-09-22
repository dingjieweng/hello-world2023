
myInt = 1
print (myInt)

#testing 
myList = ["apple","chihcken broth", "water","bear","campell"]
print (myList[3])

#objects
myDict = { "fuel_type" : "electric", "model": "S", "color": "red" }
print (myDict)
print (myDict["fuel_type"])

#strings
myNum = 1
myString = str(myNum)

#strings>array
myString = "January 5th, 1978"
myArray = myString.split(",")

# Week2 homework

myCoffee = {
"name" : "ice coffee",
"catergory" : "black",
"ice" : "light",
"sugar" : "none",
"milk" : "none"}

myPlant = {
"name" : "chinese money plant",
"color" : "green",
"Genus" : "Pilea",
"Species" : "P. peperomioides"
}

myPhone = {
"brand" : "apple",
"model" : "iPhone 7",
"color" : "black",
"functional" : True
}


person = input('Enter your name: ')
print('Hello', person)

word1 = "hello"
word2 = "world"
word3 = "You are using"
word4 = "phone"
print (word3 + " " + myPhone["brand"]+ " " + word4 +".")



# let the user know what's going on
print ("Welcome to MadLibs!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
yourName = input ( "What's your name?: ")
yourCity = input ("Where are you from? ")
yourPet = input ( "Your favorite animal? ")
adjective1 = input ( "Enter an adjective: ")
goddess1 = input( "Type a goddess: ")
location1 = input( "Your favorite city: ")
object1 = input("An object from your home: ")
importantThing1 = input("One thing you can not live without: ")
adjective2 = input("Enter one more adjective: ")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!

story = " Once upon a time," + yourName + ", a girl from "+ yourCity + " has come to " + location1 + ", carrying a " + importantThing1  \
+ " to start a new life. " \
" She has a " + adjective2 + " dream to achieve. " + " The first friend she made here, is not human. " + "It's a " +yourPet+ "." \
+ " One beautiful afternoon, " + goddess1 + " has decided to grant " + yourName + "'s wish. " \
+ yourName + "is now the richest person in the city."

# finally we print the story
print (story)