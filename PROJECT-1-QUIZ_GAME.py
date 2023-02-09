#QUIZ GAME

#prepare the list of questions
q1="""who is the king of bollywood?"
a. Salman Khan
b. Siddharth Malhotra
c. SRK
d. Aamir Khan"""

q2="""which ipl team has won the trophy maximum no. of times?
a. Mumbai Indians
b. Chennai Super Kings
c. Royal Challengers Bangalore
d. Rajasthan Royals"""

q3="""what is the first programming language?
a. C
b. B
c. FORTRAN
d. PROLOG"""

q4="""who is the founder of python?
a. Dennis Ritchie
b. Guido Van Rossum
c. Ada Lovelace
d. John Backus"""

q5="""which telugu movie song was nominated in Oscars-2023?
a. Baahubali
b. KGF
c. RRR
d. Sita Ramam"""

questions={q1:'c',q2:'a',q3:'c',q4:'b',q5:'c'}
name=input("Enter your name:")
print("Hello!",name,"Welcome to the quiz")
score=0
for i in questions:
                print()
                print(i)
                flag1=input("Do you want to skip this question?(yes/no):")
                if flag1=="yes":
                                continue
                else:
                                ans=input("Enter your answer:")
                if ans==questions[i]:
                                print("You've got one point!")
                                score=score+1
                                print("Your current score is:",score)
                else:
                                print("You've got it wrong!")
                                score=score-1
                                print("Your current score is:",score)
                flag2=input("Do you want to quit?(yes/no):")
                if flag2=="yes":
                                break
print("Your total score is:",score)
print("Thank you for playing! Have a good day")
                                
                                
