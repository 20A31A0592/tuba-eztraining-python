#Bitwise operators

'''n1,n2=int(input("Enter:")),int(input("Enter:"))
print(n1&n2)
print(n1|n2)
print(~(n1))
print(~(n2))
print(n1^n2)
print(n1<<n2)
print(n1>>n2)'''

# reading multiple inputs of integer data type

'''n=int(input("size:"))
l=list(map(int,input("Numbers:").strip().split()))[:n]
print(l)'''

# get the multiplication of 10 numbers as output

'''l=list(map(int,input("Numbers:").split()))
resu=1
for i in l:
                resu=resu*i
print(resu)'''

#delimiters

'''print("its","a","good","day",end="&&&")
print("all","is","good",sep="  ",end="&&&")
print("joy")'''

#print upside-down triangle
'''print("* * * * *")
print(" * * * * ")
print("  * * *")
print("   * *")
print("    *")
'''
#logic for normal triangle

'''n=int(input("size:"))
for i in range(n):
      for j in range(0,n-i-1):
          print(" ",end="")
      for j in range(0,i+1):
          print("*",end=" ")
      print()'''

# logic for upside down triangle

'''n=int(input("size:"))
for i in range(n):
      for j in range(0,i+11):
          print(" ",end="")
      for j in range(0,n-i-1):
          print("*",end=" ")
      print()'''

# print heart

'''print("    *    *     ")
print("  *   *    *   ")
print("   *      *   ")
print("     *  *     ")
print("       *       ")'''

#print a frog

#Conditional statements

'''temp=int(input("Enter:"))
if(temp>45):
                print("its the hottest temperature")
elif(temp>=40 or temp<=45):
                print("its hot")
elif(temp>=25 or temp<=40):
                print("its moderate")
elif(temp>=10 or temp<=25):
                print("its cold")
else:
                print("its chilled")'''

#Control Statements
#WHILE LOOP

#printing numbers 1 to 10
'''n=1
while(n<=10):
                print(n)
                n=n+1'''

#printing even numbers from 2 to 20
'''n=2
while(n<=20):
                if(n%2==0):
                                print(n)
                n=n+1'''

#printing odd numbers from 1 to 30
'''n=1
while(n<=30):
                if(n%2!=0):
                                print(n)
                n=n+1'''

#FOR LOOP

#printing numbers 1 to 10
'''for i in range(1,11):
                print(i)'''
                
#printing even numbers from 2 to 20
'''for i in range(2,21,2):
                print(i)'''

#printing odd numbers from 1 to 30
'''for i in range(1,31,2):
                print(i)'''






