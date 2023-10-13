#!python3
'''
The program will ask the user for a username and a password
If the user name and password are correct, the program will
exit and say "Access Granted".
If they are not correct, the program will say "Access Denied".
There will be a maximum of 3 guesses allowed
'''

expectedUsername = "systemadmin"
expectedPassword = "master"

password = "master"
for i in range(1,4):

    user = input("Please enter the username: ")
    passw = input("Enter your password: ")
    if user == expectedUsername and passw == expectedPassword:
        print("Access granted")
        break

    if user == expectedUsername and passw != expectedPassword:
        print("Access denied")

    if user != expectedUsername and passw == expectedPassword:
        print("Access denied ")

    if user != expectedUsername and passw != expectedPassword:
        print("Access denied ")


else:
    print("You failed")   


    #sadly it doesn't work without each if statement so im gonna keep it how it works        






    