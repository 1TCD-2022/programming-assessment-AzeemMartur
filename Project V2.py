import time
"""
Filename:main.py
Author:Abdulazeem Martur
Date: 1/07/2022
Description: This program is a anime quiz that can be played by anyone. There will be 10 questions and the user will choose 1,2 or 3 for there answer. At the end the socre will be printed.
"""
#There are 3 lists one fore questins, one for answere,and one fore the answer feed back, 
QUESTION = [
  "Q1 Who is The Main Character of Naruto?",
  "Q2 Luffy's Middle Name?",
  "Q3 What is the higest selling manga",
  "Q4 In which anime series is Ash Ketchum the main character?",
  "Q5 Who created Attack on Titan?",
  "Q6 What is Toie animation's Mascot?",
  "Q7 What type of anime is HAIKYU!!?",
  "Q8 What are the swords called in Bleach?",
  "Q9 What is the most in-demand show of 2021?",
  "Q10 Which shinigami likes apples?"
  ]
ANSWER = [
  "1.Sasuke, 2.Nagato, 3.Naruto ",
  "1.D, 2.A, 3.T ",
  "1.Dragon Ball, 2.One Piece, 3.Attack on Titan ",
  "1.Pokemon, 2.Dororo, 3.Doraemon",
  "1.Eiichiro Oda, 2.Hajime Isayama, 3.Tite Kubo",
  "1.Totoro, 2.Pero, 3.Bugs Bunny",
  "1.Fighting, 2.Sports, 3.Romance",
  "1.Zanpakutō, 2.Nichirin blade, 3.Saijō Ō Wazamono",
  "1.Kimetsu no Yaiba 2.Boruto 3. Attack on Titan",
  "1. Ryuk, 2.Rem 3.Mello"
  
]
ANSWER_FEEDBACK = ["Correct","Wrong"]
# adding points so the user know how many points they have. All the points will be printed at the end.
points=0
#I have wolcomed the user by asking there name which be later used to print the score
print("Welcome to Anime Quiz")
time.sleep(0.2)
user_name = input("What is your name ").strip()
print("Hello ",user_name)
time.sleep(0.2)
print ("The Quiz is about to start, your points will be printed at the end")
print(" ")
time.sleep(0.5)
#ask the user the questions
print (QUESTION[0])
i=0
#use wile loop to valadate the user option
while i<999999999999:
    A1 = input(ANSWER[0]+"\nChoose option 1,2 or 3 ").strip()
    if A1 == "3":
        print(ANSWER_FEEDBACK[0])
        points = points + 1
        break
    elif A1 == "1" or A1 == "2":
        print(ANSWER_FEEDBACK[1])
        break
    else:
      print("Choose valid option") 
    i+=1

print("  ")
print (QUESTION[1])
i=0
while i<999999999999:
    A1 = input(ANSWER[1]+"\nChoose option 1,2 or 3 ").strip()
    if A1 == "1":
        print(ANSWER_FEEDBACK[0])
        points = points + 1
        break
    elif A1 == "3" or A1 == "2":
        print(ANSWER_FEEDBACK[1])
        break
    else:
      print("Choose valid option") 
    i+=1
  
print("  ")

print (QUESTION[2])
i=0
while i<999999999999:
    A1 = input(ANSWER[2]+"\nChoose option 1,2 or 3 ").strip()
    if A1 == "2":
        print(ANSWER_FEEDBACK[0])
        points = points + 1
        break
    elif A1 == "1" or A1 == "3":
        print(ANSWER_FEEDBACK[1])
        break
    else:
      print("Choose valid option") 
    i+=1
  
print("  ")

print (QUESTION[3])
i=0
while i<999999999999:
    A1 = input(ANSWER[3]+"\nChoose option 1,2 or 3 ").strip()
    if A1 == "1":
        print(ANSWER_FEEDBACK[0])
        points = points + 1
        break
    elif A1 == "2" or A1 == "3":
        print(ANSWER_FEEDBACK[1])
        break
    else:
      print("Choose valid option") 
    i+=1

print("  ")

print (QUESTION[4])
i=0
while i<999999999999:
    A1 = input(ANSWER[4]+"\nChoose option 1,2 or 3 ").strip()
    if A1 == "2":
        print(ANSWER_FEEDBACK[0])
        points = points + 1
        break
    elif A1 == "1" or A1 == "3":
        print(ANSWER_FEEDBACK[1])
        break
    else:
      print("Choose valid option") 
    i+=1

print("  ")

print (QUESTION[5])
i=0
while i<999999999999:
    A1 = input(ANSWER[5]+"\nChoose option 1,2 or 3 ").strip()
    if A1 == "2":
        print(ANSWER_FEEDBACK[0])
        points = points + 1
        break
    elif A1 == "1" or A1 == "3":
        print(ANSWER_FEEDBACK[1])
        break
    else:
      print("Choose valid option") 
    i+=1

print("  ")

print (QUESTION[6])
i=0
while i<999999999999:
    A1 = input(ANSWER[6]+"\nChoose option 1,2 or 3 ").strip()
    if A1 == "2":
        print(ANSWER_FEEDBACK[0])
        points = points + 1
        break
    elif A1 == "1" or A1 == "3":
        print(ANSWER_FEEDBACK[1])
        break
    else:
      print("Choose valid option") 
    i+=1

print("  ")

print (QUESTION[7])
i=0
while i<999999999999:
    A1 = input(ANSWER[7]+"\nChoose option 1,2 or 3 ").strip()
    if A1 == "1":
        print(ANSWER_FEEDBACK[0])
        points = points + 1
        break
    elif A1 == "2" or A1 == "3":
        print(ANSWER_FEEDBACK[1])
        break
    else:
      print("Choose valid option") 
    i+=1

print("  ")

print (QUESTION[8])
i=0
while i<999999999999:
    A1 = input(ANSWER[8]+"\nChoose option 1,2 or 3 ").strip()
    if A1 == "3":
        print(ANSWER_FEEDBACK[0])
        points = points + 1
        break
    elif A1 == "2" or A1 == "1":
        print(ANSWER_FEEDBACK[1])
        break
    else:
      print("Choose valid option") 
    i+=1

print("  ")

print (QUESTION[9])
i=0
while i<999999999999:
    A1 = input(ANSWER[9]+"\nChoose option 1,2 or 3 ").strip()
    if A1 == "1":
        print(ANSWER_FEEDBACK[0])
        points = points + 1
        break
    elif A1 == "2" or A1 == "3":
        print(ANSWER_FEEDBACK[1])
        break
    else:
      print("Choose valid option") 
    i+=1

print("Clacutaing score.....")

time.sleep(3.5)

# the amount of points the user got will be printed here.
print("{} got {} out of 10".format(user_name,points))
