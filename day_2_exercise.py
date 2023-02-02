
#program1
#get a number as input and find out whether it is 500 or not?

'''number= int(input("Enter the number to be checked:"))
if(number == 500):
                print("Yes, the number is:",number)
else:
                print("No, the number is:",number)'''

#program2
#check the number is even-positive or odd-positiveor even-negative
#or odd-negative

'''number=int(input("Enter the number to be checked:"))
if(number%2==0):
      if(number>0):
                      print("The number",number," is even-positive")
      else:
                      print("The number",number,"is even-negative")
elif(number%2!=0 and number>0):
                print("The number",number,"is odd-positive")
else:
                print("The number",number,"is odd-negative")'''

#program3
#get 2 numbers and find out the biggest number

'''n1,n2=int(input("Enter:")),int(input("Enter:"))
if(n1>n2):
                print("The number n1:",n1,"is the biggest number")
else:
                print("The number n2:",n2,"is the biggest number")'''

#program4
#check given number is float or integer

'''number=input("Enter:")
if "." in number:
             print("the number:",number,"is a float")
else:
                print("the number:",number,"is an integer")'''
#another approach
'''number=12.3
isinstance(number,float)
if(True):
                print("the number:",number,"is a float")
else:
                print("the number:",number,"is an integer")'''
#another approach
'''n=12.3
if(n==int(n)):
                print("the number is integer:",n)
else:
                print("the number is float:",n)'''
#another approach
'''n=1.6
if(n%1==0):
                print("the number is integer:",n)
else:
                print("the number is float:",n)'''
#another approach
n=4.0
result=(n-int(n))
if(result>0 or result!=0):
                print("the number is float:",n)
else:
                print("the number is integer:",n)
                
#program5
#get 3 numbers and find the biggest number

'''n1,n2,n3=int(input("Enter:")),int(input("Enter:")),int(input("Enter:"))
if((n1>n2) and (n1>n3)):
                print("n1:",n1,"is the biggest number")
elif((n2>n1) and (n2>n3)):
                print("n2:",n2,"is the biggest number")
else:
                print("n3:",n3,"is the biggest number")'''

#program6
#number is divisible by 11 or not

'''number=int(input("Enter:"))
if(number%11==0):
                print("The number:",number,"is divisible by 11")
else:
                print("The number:",number,"is not divisible by 11")'''

#program7
#number is divisible by both 2 and 5

'''number=int(input("Enter:"))
if(number%2==0 and number%5==0):
                print("The number:",number,"is divisible by both 2 and 5")
else:
                print("The number:",number,"is not divisible by both 2 and 5")'''
                









                
