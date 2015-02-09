__author__ = 'ayg9fh'

from Crypto.Hash import SHA256

user_pass = {}

username = input("Please enter a username: ")
password = input("Please enter a password: ")

# Continuously gather usernames and passwords
while username and password:
    print("Got a username and password")
    print(username, password)
    pass_hash = SHA256.new(str.encode(password)).hexdigest()
    user_pass[username] = pass_hash

    username = input("Please enter a username: ")
    password = input("Please enter a password: ")
print("Received empty lines, moving to login sequence.")
print(user_pass)

# Continuously try to log in
test_username = input("Please enter a username to login: ")
test_password = input("Please enter that user's password: ")
while test_password and test_username:
    # Compute the hash of the potential password
    test_pass_hash = SHA256.new(str.encode(test_password)).hexdigest()
    if test_username not in user_pass:
        print("User not found.")
    elif user_pass[test_username] == test_pass_hash:
        print("Login successful.")
    else:
        print("Login fails.")

    test_username = input("Please enter a username to login: ")
    test_password = input("Please enter that user's password: ")

print("Received empty lines, terminating logon.")
