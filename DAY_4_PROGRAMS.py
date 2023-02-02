
#Dictionary comprehension
'''d={n:n*n for n in range(1,5)}
print(d)'''

# calculating the product price for 5 units
'''old = {"rice":30,"daal":20,"oil":40}
new = {product:price*5 for (product,price) in old.items()}
print(new)'''

# with some conditions or checks
'''real = {"p":10,"u":20,"t":25,"s":24}
now = {name:age for (name,age) in real.items() if(age>20)}
print(now)'''

#create a list with 8 customer names display a dictionary which has customer
#names along with discounts for them from a particular shop

'''import random
customer = list(map(str,input("Enter customer names:").split()))
print(customer)
d={cname:random.randint(1,50) for cname in customer  }
print(d)'''

#creating a dictionary from 2 lists
'''l1=['a','b','c']
l2=[1,2,3]
d={k:v for (k,v) in zip(l1,l2)}
print(d)'''

#create 2 list student names-5 and total marks of 5 students out of 100
#for 5 subjects display a dictionary with these lists with values= percentage
'''l1=list(map(str,input("Enter names:").split()))
l2=list(map(int,input("Enter total marks out of 500:").split()))
l3=[]
for i in l2:
                i=(i/500)*100
                l3.append(i)
d={names:percent for (names,percent) in zip(l1,l3)}
print(d)'''
#another approach
import random
'''l1=list(map(str,input("Enter names:").split()))
l2=[]
for i in range(len(l1)):
                a=(random.randint(100,500)/500)*100
                l2.append(a)
print(l2)
d={names:percent for (names,percent) in zip(l1,l2)}
print(d)'''
#another approach
'''import random
l1=list(map(str,input("Enter names:").split()))
l2=[]
percent=[]
for i in range(len(l1)):
                a=random.randint(100,500)
                l2.append(a)
                b=(a/500)*100
                percent.append(b)
print(l2)
d={names:percent for (names,percent) in zip(l1,percent)}
print(d)'''

#strings

'''s="hi my name is tuba"
print(s.upper())
print(s.lower())
print(s.casefold())
print(s.capitalize())
print(s.replace('a','u'))
print(s.strip())
print(s.split())
print(s.center(30,'*'))
print(s.count('a'))
print(s.count('a',12,len(s)))
print(s.endswith(' ',0,len(s)))
print(s.endswith(' '))
print(s.find('a',0,len(s)))
print(s.find('x',0,len(s)))
print(s.find('a'))
print(s.index('a',12))
print(s.islower())
print(s.isupper())
print(s.istitle())
print(max(s))
print(min(s))
print(s.startswith('hi'))
print(s.rfind('a',len(s)))
print(s.rfind('a',0,len(s)))
print(s.index('x',0,len(s)))'''

#output
'''HI MY NAME IS TUBA
hi my name is tuba
hi my name is tuba
Hi my name is tuba
hi my nume is tubu
hi my name is tuba
['hi', 'my', 'name', 'is', 'tuba']
******hi my name is tuba******
2
1
False
False
7
-1
7
17
True
False
False
y
 
True
-1
17'''

#one string as input along with a character find out and display whether the
#character is present or not

'''s=str(input("enter the string:"))
ch=str(input("enter the character:"))
for i in ch:
                if ch in s:
                                print("the character:",i,"is equal to:",ch)
                else:
                                print("not present")'''

#another approach
'''s=str(input("enter the string:"))
ch=str(input("enter the character:"))
if ch in s:
                print("present")
else:
                print("not")'''

#check whether the string is palindrome or not
'''s1=str(input("enter s1:"))
s2=s1[::-1]
if s1 is s2:
                print("palindrome")
else:
                print("not")'''

#another approach
'''s=str(input("enter:"))
l=[s[x] for x in range(len(s)-1,-1,-1)]
print(l)
if l is s:
                print("palindrome")
else:
                print("not")'''

#take string as input check string contains space or not if yes count no. of
#spaces and print
'''s=str(input("enter:"))
count=0
if " " in s:
                print("yes")
else:
                print("no")
for i in s:
                if(i==" "):
                                count=count+1                                
print(count)'''

#check whether the number is neon or not

'''n=int(input("enter:"))
s=n*n
suml=0
while s>0:
                i=s%10
                suml=suml+i
                s=s//10
if(n == suml):
                print("neon")
else:
                print("not")'''

#check the list contains neon or not
l=list(map(int,input("enter:").split()))
l1=[]
sum1=0
for i in l:
                n=i*i
                l1.append(n)
for i in l1:
                while(i>0):
                                sq=i%10
                                sum1=sum1+sq
                                i=i//10
                if(sum1 == i):
                                print(i)
#another approach
import math
l=list(map(int,input("enter:").split()))
for i in l:
                sq=math.pow(i,2)
                sum=0
                while(sq>0):
                                n=sq%10
                                sum=sum+n
                                sq=sq//10
                
                if(sum == i):
                                print(i)
                
                
                
                
                

#another approach
'''num = int(input("Enter a number \n"))
sqr = num*num #square of num
sumOfDigit = 0

#calculating sum of digits of sqr
while sqr>0:
    sumOfDigit =sumOfDigit + sqr%10
    sqr = sqr//10

if (num == sumOfDigit):
    print("Neon Number \n")
else:
    print("Not a Neon Number \n")'''
                
#create a list with vowels get a string as input and count vowels
# from the string and display the result

'''l=['a','e','i','o','u']
s=str(input("enter:"))
count = 0
for i in s:
                if i in l:
                                count=count+1
print(count)'''
                                






      
