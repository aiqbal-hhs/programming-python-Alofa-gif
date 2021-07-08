print("Hello user welcome to a quiz today the subject is about games this quiz will include a score count and please read the question properly. anyways good luck and try to Answer some of the questions correctly")

Question_1 = input ("What was the first game ever made in the 1958, a: Tennis game, b: baseball game, c: Basketball game")
score = 0

if Question_1 == 'A' or Question_1 == 'a':
    print("Correct")
    score = score + 1
else:
    print("Incorrect Tennis game or tennis game")
    score = score - 1

Question_2 = input ("A famous game named battlefield 1 is based on historical history but what events was this game inspired by, a: World war 3, b: World war 2, c: World war 1")

if Question_2 == 'C' or Question_2 == 'c':
    print("Correct")
    score = score + 1
else:
    print("Incorrect world war 1 or World war 1")
    score = score - 1

Question_3 = input ("In 2017 a famous battle royale game was released, everyone should have this one, a: Black ops 3, b: Fortnite, c: PUBG")

if Question_3 == 'B' or Question_3 =='b':
    print("Easy Right?")
    score = score + 1
else:
    print("I get it sometimes we dont know these stuff fortnite/Fortnite")
    score = score - 1

Question_4 = input ("The owner of Minecraft is markus persson What is his Nationality a: French, b: German, c: Swedish")

if Question_4 == 'C' or Question_4 == 'c':
    print("Correct")
    score = score + 1
else:
    print("Nice try Swedish/swedish")
    score = score - 1

Question_5 = input ("Respawn Entertainment Join a money laundering company and the worst ones so fair, but has Successfully made a famous game from to 2019-2021 What was the name of this specific Company a: EA, b: DICE, c: Frostbite")

if Question_5 == 'A' or Question_5 == 'a':
    print("EA is the worst, anyways Good job")
    score = score + 1
else:
    print("I am sorry for such a confusing question I just like Respawn Entertainment and its work")
    score = score - 1

Question_6 = input ("A company began making gaming headsets and created the first ever gaming headset for game consoles with the launch of the X51 what year were the first headset released at, a: 2005, b: 2007, c: 2001")

if Question_6 == "A" or Question_6 == 'a':
    print("how did you know that?")
    score = score + 1
else:
    print("Incorrect in the year 2005")
    score = score - 1

Question_7 = input ("referring to the first question, who is the founder of this first game, a: Albert Einsten, b: Willam Higinbotham, c: Kenneth G. Wilson ")

if Question_7 == "B" or Question_7 == 'b':
    print("Correct this was the last question")
    score = score + 1
else:
    print("hey at least you tried its Willam this was the last question")
    score = score - 1

print("good job you scored {}/7 questions".format(score))
 
