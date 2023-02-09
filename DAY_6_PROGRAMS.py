#exception handling
#program1
'''a=100
b=0
try:                      #u are telling this may have an error,u try
                print(a/b)
except Exception as e:     #if there is an error i will handle it
                print("its an error:",e)
finally:                 #gets executed even if there is an error or not
                print("done!")'''

#program2
#whenever you open a file make sure you close it
'''a=10
b=0
try:
                print("resource or file is open")
                print(a/b)
except Exception as e:
                print("the error is:",e)
finally:
               print("done!")'''
#direct exception given
'''a=10
try:
                b=int(input("enter b:"))
                print(a/b)
except ZeroDivisionError as e:
                print("its an error:",e)
finally:
                print("done!")'''

#program3
#specific error-specific exception
#single try-multiple exceptions
'''a=10
try:
                b=int(input("enter b:"))
                print("the resource is open")
                print(a/b)
except ZeroDivisionError as e:
                print("its an error:",e)
except ValueError as e:
                print("its an error:",e)
except Exception as e:
                print("its an error:",e)
finally:
                print("done!")'''

#raising a user-defined exception
'''x=int(input("enter a number:"))
if(x%2!=0):
                raise Exception("it should be an even no.")
else:
                print("proceed..")'''
#OOPS CONCEPTS
#creation of a class and its objects
'''class birds:      #creation of a class
                def type(self):       #creation of a method in a class
                                print("its a bird")
pigeon=birds()        # creation of an object1
pigeon.type()          # accessing the method of the class using . operator

crow=birds()           #object2
crow.type()'''

#a class without a method
'''class computer:
                print("hrllo")
obj=computer()'''

#constructor
'''class Employee:
                def __init__(self,name,id):
                                 self.name=name
                                 self.id=id
#method with _ is dundard method & a constructor
                def display(self):
                                print(self.name,self.id)
obj1=Employee("h",12)
obj2=Employee("i",20)
obj1.display()
obj2.display()'''

#variables and variable access in class and method
'''class computer:
                a=10        #global scope and class variables a&b
                b=20
                print("class or instance variable:",a,b)
                def display(self):
                                c=100      #local scope
                                print("local variable:",c)
                                print("class variable inside method:",self.a)
obj1=computer()
print(obj1.a)
print("sum:",obj1.a+obj1.b)
obj1.display()
obj2=computer()
print(obj2.b)
print(obj1.c)'''










                
