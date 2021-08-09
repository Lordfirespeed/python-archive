
attempts = 0

while attempts < 3:

    username = input("Username: ")
    pwd = input("Password: ")

    if (username.title() == 'Amy') and (pwd == 'bob'):
        print("Welcome " + username.title() + ", how are you?")
        break

    else: 
        print("Wrong username or password, please try again")
        #You wrote: attempts = +1
        attempts += 1

if attempts >= 4:
    print("Your account has been locked")
    
