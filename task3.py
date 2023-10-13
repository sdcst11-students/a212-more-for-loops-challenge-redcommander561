#!python3

"""
Similar to task2.py
Program will ask the user to enter their username and password
If the username is a match, see if the password is the correct one
annie's password is 12345
betty's is password
etc.

"""

users = ["annie","betty","charles","doug","eddie","flon"]
passwords = ["12345","password","iloveyou","mom","default","0"]


user = input("Enter username: ")
passw =input("Enter password: ")

answer = False

for i in range(6): 
    if user == users[i]:
        if passw == passwords[i]:
            print("Login successful")
        else:
            print("Login failed. Incorrect password for the given username.")
        answer = True
        break

else:
    print("Login failed. Username not found.")