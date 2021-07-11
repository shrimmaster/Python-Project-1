guessNumber=int(input("Enter the number I am thinking about , choose one from 1-9"))
if(guessNumber>6):
    print("Your guess was to high ! try again")
elif(guessNumber>4):
    print("You got it , Congrats you won !")
else:
    print("Your guess was to low . Try again !")
    
