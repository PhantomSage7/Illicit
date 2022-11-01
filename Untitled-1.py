#Suppose a Hotel has 20 rooms, at the max there can be 4 persons sharing a room. The cost
# of stay per night is Rs 500 per room. If there are more than 2 people in a room, the price of
# room increases by Rs 500 per person extra staying in the room.
# Write/Design a python program in such a way that in the Dictionary the room numbers are
# stored as keys; the Details for boarders (Name, Sex, Age, and Contact Number) are stored in
# a list and assigned with the keys accordingly (use nested list).
# (Assuming that all rooms are Empty in the beginning) Whenever new borders visit, ask for
# how many nights they want to stay, check if rooms are available or not, accordingly allot
# them a room, store their details accordingly (all should be given as input via the user). Use
# Menu-Driven Programming approach with if-else statements and an infinite loop that
# breaks on the condition that in total there are 70 borders in the Entire Hotel or all rooms are
# filled.
# At the end, calculate the revenue generated per room, and find the total income. Check
# how many rooms are still empty, and print the available room numbers in a suitable way.
# Store the entire Data of the bookings in a txt file.

# [Note:- You can take Reference from resources, but the code should be completely yours,
# with output. Note that the code should be redundant, and the entire code should run in one
# cell, while using Jupyter Notebook or Google Colab. Mention your ‘Roll_Name’ in the
# filename, send the files in “.ipynb (python notebook)” format]
import numpy as np

Dict = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[],14:[],15:[],16:[],17:[],18:[],19:[],20:[]}

i = 0
j = 0

for i in range(0,2):

  print("Room",i+1,"\n")
  n = int(input())

  for j in range(0,n):
    print("Occupant",j+1,"\n")
    print("Enter name: ")
    name = str(input())
    print("Enter gender: ")
    sex = str(input())
    print("Enter age: ")
    age = int(input())
    print("Enter contact number: ")
    number = int(input())

    List = [name,sex,age,number]
    Dict[i+1] += 1[List]

    print("\n")

print(Dict)
len(Dict[1])
