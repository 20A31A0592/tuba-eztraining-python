
#random module
import random as r
'''x="hello good mrng"
print(r.sample(x,3))
l=[1,2,3,4,5]
print(r.sample(l,3))
t=(1,2,3,4,5)
print(r.sample(t,3))'''
#it gives different o/p everytime

'''l=[1,2,3,4,5]
r.shuffle(l)
print(l)
x="hello good"
r.shuffle(x)
print(x)       not support string'''

'''b=[1,2,3,4]
print(r.choice(b))
x="hello"
print(r.choice(x))
t=(1,2,3,4)
print(r.choice(t))'''


'''print(r.random()) 

print(r.randint(10,50))'''

'''l=[106,200,308,400,505]
print(r.choices(l,k=10))
print(r.choices(l,m=10))
'''
#only k is supported

'''print(r.uniform(10,20))'''

#calendar module
#import calendar as cd

'''print(cd.calendar(2023))

#print(cd.month(2023,1))

#print(cd.setfirstweekday(cd.FRIDAY))
#print(cd.calendar(2023))'''

#datetime module

#functions

#1.without arguments and without return value

'''def sample():      #function definition or description
                print("hello")
                print("hi")
sample()         # function call
print("good")
sample()'''
#multiplication of 3 numbers using functions

'''def multi():
                a=int(input("enter a:"))
                b=int(input("enter b:"))
                c=int(input("enter c:"))
                mul=a*b*c
                print(mul)
multi()'''

#2.without arguments and with return value

'''def sum():
                a=int(input("enter a:"))
                b=int(input("enter b:"))
                c=int(input("enter c:"))
                add=a+b+c
                return add
result=sum()
print(result)'''

#3.with arguments and without return value

#dynamic i/p
'''def diff(d,e,f):
                sub=d-e-f
                print(sub)
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
diff(a,b,c)'''

#static i/p
'''def diff(d,e,f):
                sub=d-e-f
                print(sub)
diff(4,2,1)'''

#4.with arguments and with return value

#dynamic i/p
'''def prod(d,e,f):
                mul=d*e*f
                return mul
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
result=prod(a,b,c)
print(result)'''

#static i/p
'''def prod(d,e,f):
                sub=d*e*f
                return sub
result = prod(4,2,1)
print(result)'''
                
#program1:Lemons program using type 1
'''def lemons():
                n=int(input("enter the no. of lemons:"))
                ng=3
                if(n==21):
                                print("sufficient!")
                elif(n>21):
                                print("you have excesss:",(n-21),"lemons")
                else:
                                print("you need:",(21-n),"lemons")
lemons()'''

#program2:Find factors of the given number using type 2
'''def fact():
                n=int(input("enter a number:"))
                f=1
                l=[]
                while(f<n+1):
                                if(n%f==0):
                                                l.append(f)
                                f=f+1
                return l
                                
result=fact()
print(result,end="")'''
#another approach
'''def fact():
                n=int(input("enter:"))
                l=[]
                for i in range(1,n+1):
                                if(n%i==0):
                                                l.append(i)
                return l
result=fact()
print(result)'''
                                
#program3:Print multiplication table of a number using type 3
'''def mul(a):
                for i in range(1,11):
                                print(n,"X",i,"=",(n*i))
n=int(input("enter number:"))
mul(n)'''

#program4:Find out sum of digits of given number using functions type4
'''def sod(n):
                su=0
                while(n>0):
                                s=n%10
                                su=su+s
                                n=n//10
                return su
a=int(input("enter a:"))
result=sod(a)
print(result)'''
#sum of numbers in a list
'''def add(l):
                sum=0
                for i in l:
                                sum=sum+i
                return sum                                
a=list(map(int,input("enter numbers:").split()))
result=add(a)
print(result)'''
#recursion
'''def display():
                n=int(input("enter:"))
                if(n==1):
                                display()
                else:
                                print("done!")
display()'''

#factorial calculation using recursion
'''def fact(n):
                if(n==1 or n==0):
                                return 1
                else:
                                s=n*fact(n-1)
                return s
a=int(input("enter n:"))
result=fact(a)
print(result)'''

#fibonacci numbers
#logic
'''num=int(input("enter no. of fibonacci numbers:"))
n1,n2=0,1
print("fibonacci series is:",n1,n2,end=" ")
for i in range(2,num):
                n3=n1+n2
                n1=n2
                n2=n3
                print(n3,end=" ")
print()'''
#using function
'''def fibo(n):
                if n<0:
                                print("incorrect i/p")
                elif(n==1):
                                return 0
                else:
                                return (fibo(n-1)+fibo(n-2))
n=int(input("enter:"))
result=fibo(n)
print(result)'''
                                
#function returns more values
#addition subtraction of 2 numbers in 1 function
'''def add_sub(a,b):
                add=a+b
                sub=a-b
                return add,sub
a,s=list(map(int,input("enter:").split()))
result=add_sub(a,s)
print(result)'''

#variable length method
'''def sum(*a):
                c=0
                for i in a:
                                c=c+i
                print(c)
sum(10,2,8,0)'''

#keyword method
'''def names(name,age):
                print(name,age)
names(age=11,name="aamena")'''
#default
'''def add(a=300,b=200):
                c=a+b
                print(c)
add(500,500)
add(40,50)
add(100)   #the value is added to the above value of b'''
                                                
                

                
                


