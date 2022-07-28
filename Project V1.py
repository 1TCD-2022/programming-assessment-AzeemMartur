import time
"""
Filename:main.py
Author:Abdulazeem Martur
Date: 1/07/2022
Description: This 
"""
QUESTION = [
  "Q1 Who is The Main Character of Naruto?",
  "Q2 Luffy's Middle Name?",
  "Q3 What is the higest selling manga"
  
  ]
ANSWER = [
  "1.Sasuke, 2.Nagato, 3.Naruto ",
  "1.D, 2.A, 3.O ",
  "1.Dragon Ball, 2.One Piece, 3.Attack on Titan "
]
ANSWER_FEEDBACK = ["Correct","Wrong"]

print("Welcome to Anime Quiz")
time.sleep(1)
user_name = input("What is your name ").strip()
print("Hello ",user_name)
time.sleep(0.5)
print ("The Quiz is about to start, there will be a 1 sec break before every question")
time.sleep(2)#giving user time to read
print("The quiz Begins in")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
#ask the user the questions
print (QUESTION[0])
i=0
#use wile loop to valadate the user option
while i<999999999999:
    A1 = input(ANSWER[0]+"\nChoose option 1,2 or 3 ").strip()
    if A1 == "3":
        print(ANSWER_FEEDBACK[0])
        break
    elif A1 == "1" or A1 == "2":
        print(ANSWER_FEEDBACK[1])
        break
    else:
      print("Choose valid option") 
    i+=1

print("  ")
time.sleep(1)
print (QUESTION[1])
i=0
while i<999999999999:
    A1 = input(ANSWER[1]+"\nChoose option 1,2 or 3 ").strip()
    if A1 == "1":
        print(ANSWER_FEEDBACK[0])
        break
    elif A1 == "3" or A1 == "2":
        print(ANSWER_FEEDBACK[1])
        break
    else:
      print("Choose valid option") 
    i+=1
print("  ")
time.sleep(1)
print (QUESTION[2])
i=0
while i<999999999999:
    A1 = input(ANSWER[2]+"\nChoose option 1,2 or 3 ").strip()
    if A1 == "2":
        print(ANSWER_FEEDBACK[0])
        break
    elif A1 == "1" or A1 == "3":
        print(ANSWER_FEEDBACK[1])
        break
    else:
      print("Choose valid option") 
    i+=1
