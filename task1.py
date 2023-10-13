#!python3

'''
Create a number guessing game
There is a limit of 10 guesses
The program will ask the user to enter an integer from 1 to 100
The program will then tell the user if the number is too high, too low or correct.
If the number is correct, the program will end
If the 10 guesses are used up, the program will say that the user has lost
'''
number = 4
for i in range(1,11):
    guess1 = int(input("Enter a number from 1 to 100: "))
    if guess1 > number:
        print(f"{guess1} too high, try guessing lower: ")

    if guess1 < number:
        print(f"{guess1} is too low")

    if guess1 == number:
        print(f"{guess1} is right! Good job.")
        break


else:
    print("you failed")

    
