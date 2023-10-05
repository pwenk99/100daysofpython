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

#Write your code below this line 👇

print("You awake on beach. Remnants of your wrecked ship scattered around you.")
print("To the left you see dense jungle. To the right you see a rocky shore.")
ans1 = input("Which way do you go? Left or Right? ")

if ans1.lower() == "left":
  print("You walk into a dense jungle and find a lagoon obscured by mist.")
  ans2 = input("Do you swim across or wait to see what happens? Answer in one word. ")
  if ans2.lower() == "wait":
    print("Your patience is rewarded! A dinghy magically rises from the logoon and floats toward you.\nYou hop on and it moves to a small island in the center of the lagoon.\nAppearing before you, no longer obscured by the mist, an ancient temple with three colored doors looms ominiously a few feet from the waters edge.")
    ans3 = input("You see a red door, a blue door, and a yellow door. Which do you enter? ")
    if ans3.lower() == "red":
      print("You open the red door and enter a dark room. The door closes behind you and several torches suddenly alight, revealing a room with blackened walls and a pile of charred bones at the center.\nBefore you can react, gouts of flame erupt from the torches, burning you alive.\nYour charred remains will serve as a warning for any foolish enough to enter.")
    elif ans3.lower() == "blue":
      print("Entering the blue door you see a large stone room in the shape of an oval. A metal grate covers a round part of the center.\nYou examine the grate and see remnants of blood draining to a cavern below.\nSuddenly, a lattice gate opens to your left, and feral tiger pounces on you.\nYou try to fight it off but it over powers you easily. It bites into your neck, and the last thing you hear before you blackout are your gurgling screams.")
    elif ans3.lower() == "yellow":
      print("You reach for the yellow door and it magically opens before you touch it.\nA moss and vine covered room lies beyond the entry way.\nAt the center of the room, illuminated by a shaft of light, a green, fist-sized crystal floats above a pedestal.\nYou quickly snatch the crystal as if you're about to run from the room, but are instead filled with a coursing energy.\nYou stop in your tracks, look up, and fly through the ceiling.")
    else:
      print("You decide you've had enough choice for one day. You jump back in the dinghy, walk through the jungle, and enjoy a relaxing say at the beach.")
  else:
    print("You throw caution to the wind and dive in the misty lagoon.\nLooking under the water, you quickly realize your mistake. Corpses litter the floor beneath the cool waters.\nBefore you can surface, a legion of eels attack you from all angles.\nTheir bites seem to paralize you, and you sink to the bottom as they nibble away at your flesh.")
else:
  print("After climbing some rocky outcroppings you turn to enjoy the view.\nBut don't notice the large hole in front of you, and you fall to your death.")