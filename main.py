print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
direct1 = input('You have come to the end of the path in the forest, you have two directions to choose. \n Which way do you go, "left" or "right"? ').lower()


if direct1 == "left":
   lake = input('You are now at a beautiful lake. You can either swim or wait for a boat. Enter swim if you want to "swim", \n or "wait" if you are going to wait for a boat ').lower()
   if lake == "wait":
     island = input('You made it safely across the beautiful lake. You walked into a dungeon. There are three paths you can take each with different color plates: red, yellow, and blue. \n To enter type "red", "yellow", or "blue" ').lower() 
     if island == "red":
       print("There is a giant serpant that wraps around you. GAME OVER")
     elif island == "yellow":
        print("THROUGH YOUR PERILIS JOURNEY YOU REACHED TOMB AND FOUND THE TREASURE! RICHES FOR LIFE! YOU WON!!")
     elif island == "blue":
        print("The path you have chosen lead you to beasts driven mad by hunger. You have been eaten. GAME OVER") 
     else:
        print("You chose a secret room full of emptiness. Good bye.")
   else:
      print("Sirens have lured you with their song into the deep. GAME OVER")
else:
  print("Sadly, you wondered deeper into the forest where a giant ogre awaits. He crushed you, GAME OVER.")


  
     


 

  
       

