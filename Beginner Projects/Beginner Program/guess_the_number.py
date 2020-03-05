import random           #importing the necessary
flag=0
tries=3                 #number of tries

#create a function to check the entered number and the number generated by the program is same or not
def output(number,generated):

#if the entered number and the generated number are equal, then the if condition is performed
  if number == generated:
    print("Congrats, you guessed my number")
    global flag,tries      #setting both variables as global variables
    flag=1      #setting the flag to 1

#if the entered number is greater than the generated number, then the elif condition is performed
  elif number > generated:
    print("your guess is high")
    tries-=1    #the number of tries gets reduced by 1
    print("Remaining Tries: ",tries)

#if the entered number is less than the generated number, then the else condition is performed
  else:
    print("your guess is low")
    tries-=1
    print("Remaining Tries: ",tries)

name=input("Hello! What is your name?\n")       #To input the name of the user

print('Well, ',name,', I am thinking of a number between 1 and 20')

ran=random.randint(1,20)      #this statement will randomly pick a number between 1 and 20 and will stored in ran

for index in range(0,3):      #as the number of tries is 3, the loop will execute 3 times
  if flag==0:                 #this condition is to check whether the user guessed the correct number or not
    print('Take a guess...')
    first=int(input())        #this will be the number entered by the user
    output(first,ran)         #calling the output function
if flag==0:
  print('Sorry the correct number was ',ran)      #if the user fails to guess the number, this will print the generated number
