
import random      
import string

def randomPassword():
    
    password = random.choice(string.ascii_lowercase)                                  # Atleast one lowercase
    password += random.choice(string.ascii_uppercase)                                 # Atleast one uppercase
    password += random.choice(string.digits)                                          # Atleast one number
    password += random.choice(string.punctuation)                                     # Atleast one special characters
    randomSource = string.ascii_letters + string.digits + string.punctuation          # Generate remaining password

    for i in range(6):                                                                # Adding remaining password
        password += random.choice(randomSource)

    passwordList = list(password)                                                     # Converting into list
    random.SystemRandom().shuffle(passwordList)                                       # Shuffling the letters
    password = ''.join(passwordList)                                                  # Converting list to string
    return password

print ("Generate new password...")                                           
print ("Random Password is ", randomPassword())                                       # Output

while True:                                                                           # Retry loop and quit
    a = str(raw_input("y/n: "))
    if a == "y":
        print ("Random Password is ", randomPassword())
    elif a == "n":
        print("Done")
        break
    else:
        print("unknown answer")
