
#create a list
'''l=[1,2,3,4,5]
for i in l:
                print(i)  '''   #it gives the values as output
#create a list
'''l=[1,2,3,4,5]
for i in range(len(l)):
                print(i)  '''  #it gives the index as output

#program1
#create a list with 10 items & print items one by one

'''l=[1,2,3,4,5,6]
for i in range(len(l)):
                print(l[i])'''

#program2
#take 5 float no.s in a list and find out sum & average of the list

'''l=[1.1,2.2,3.3,4.4]
suml=0
avg=0
for i in l:
                suml=suml+l
avg=(suml/len(l))
print("sum is:",suml,"avg is:",avg)'''

#program3
#create a list with user input and display even no.s

'''l=[]
n=int(input("size:"))
even=[]
odd=[]
print("Enter numbers:")
for i in range(n):
                a=int(input())
                l.append(a)
print(l)
for i in l:
                if(i%2==0):
                                even.append(i)
                else:
                                odd.append(i)
print(even)
print(odd)'''

#another method
'''l=list(map(int,input("Enter numbers:").split()))
print(l)
even=[]
odd=[]
i=0
while i<len(l):
                if(l[i]%2==0):
                                even.append(l[i])
                else:
                                odd.append(l[i])
                i=i+1

print(even)
print(odd)'''

#create a list and find product if product<750 print sum else print product

'''l=list(map(int,input("Enter numbers:").split()))
print(l)
product=1
suml=0
for i in l:
       product=product*i
       suml=suml+i
if product<750:
       print("sum is:",suml)
else:
       print("product is:",product)'''

# creates a list from the existing list

'''l=["hello","hii","good","bye"]
c=[]
for n in l:
                if "h" in n:
                                c.append(n)
print(c)'''

#list comprehension

'''l1=[2**x for x in range(2,10)]
print(l1)'''

'''l2=[a for a in range(100,120,2)]
print(l2)'''

l3=[1,2,3,4,5,6]
l4=[i for i in l3 if(i<5)]
print(l4)



                
       





