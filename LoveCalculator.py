print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
tcount = (name1.lower().count("t")) + (name2.lower().count("t"))
rcount = (name1.lower().count("r")) + (name2.lower().count("r"))
ucount = (name1.lower().count("u")) + (name2.lower().count("u"))
ecount = (name1.lower().count("e")) + (name2.lower().count("e"))

Tens = tcount + rcount + ucount + ecount

lcount = (name1.lower().count("l")) + (name2.lower().count("l"))
ocount = (name1.lower().count("o")) + (name2.lower().count("o"))
vcount = (name1.lower().count("v")) + (name2.lower().count("v"))

Ones = lcount + ocount + vcount + ecount

score = Tens * 10 + Ones

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print (f"Your score is {score}.")