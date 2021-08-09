password = ""
def password_correct(password):
    return ((len(password) >= 9) and (len(password) <= 12))
while not password_correct(password):
    password = input('Enter password between 9 and 12 character length.\n> ')
    if password_correct(password):
        print('Password accepted.')
        break
    else:
        if len(password) < 9:
            print('Password too short.')
        else:
            print('Password too long.')
    
