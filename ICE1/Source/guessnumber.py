import random
while 0==0:
 n= random.randint(0,9)
 print('guess', n)
 n1=input("Enter a guess")
 guess=int(n1)
 if guess == n:
     print("Number guessed by the user is correct")
     break
 elif guess > n:
        print("Number guessed is above the actual value")
 else:
        print("Number guessed by the user is below the actual vale")

