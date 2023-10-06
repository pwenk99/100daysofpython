rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
npcChoice = random.randint(0,2)
rpsList = [rock, paper, scissors]

if choice >= 3 or choice < 0:
  print("That's not one of the right numbers. Try again but for realsies...")
else:
  print(rpsList[choice])
  print("\nComputer chose:")
  print(rpsList[npcChoice])
  if choice == npcChoice:
    print("It's a draw!")
  elif choice == 0 and npcChoice == 2:
    print("You win!")
  elif choice < npcChoice:
    print("You lose!")
  elif choice == 2 and npcChoice == 0:
    print("You lose!")
  elif choice > npcChoice:
    print("You win!")