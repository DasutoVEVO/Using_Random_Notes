#Notes for creating random numbers!
#October 2022

#import the libraries of random numbers
import random


#random float numbers




#If the random value creating sentence is inside a loop, the variable will be redefined each time.
for counter in range(3):
    number1 = random.random() #0-1
    number2 = random.uniform(1,10)#Between A and B

    print("")
    print("")
    print("Your random float number between 0 and 1 is: ",number1)
    print("")
    print("")
    print("Your random float number between 1 to 10 is: ",number2)


#random integers

    number3=random.randrange(5) #0-x [5] not including 5, it stops
    number4=random.randrange(10,100,5) #start,stop,step
    number5=random.randint(2,8) #A to B including B

    print(number3)
    print(number4)
    print(number5)


#random choice from a list

    myList = ["A","B","C"]
    print(random.choice(myList))


