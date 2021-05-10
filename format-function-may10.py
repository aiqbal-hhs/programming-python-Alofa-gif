name = input("What is your name?")
surname = input("What is your surname")
age = input("How old are you?")
Nationality = input("What country are you legally authorized from")

print("So information I have is {} {} {} {}".format(name, surname, age, Nationality))
Correction = input("Do you wish to restart your answer you have answered with say something other than a word is same as yes, or say yes to stay with answers.")

if Correction == "yes":
  print("very well then")
else:
  print("Alright so to restart you either refresh the page or press ok")
