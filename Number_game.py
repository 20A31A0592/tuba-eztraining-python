import random
n = random.randrange(1,50)
guess = int(input("enter the number:"))
while n!=guess:
                if guess<n:
                                print("Too low!")
                                guess = int(input("Enter another number:"))
                elif guess>n:
                                print("Too High!")
                                guess = int(input("Enter another number:"))
                else:
                                break
print("You guessed it right!")
