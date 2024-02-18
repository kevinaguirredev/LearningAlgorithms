import random
import string

def generateRandomPassword(length):
    
    assert(length >= 4), "Password length must be at least 4 characters in length"

    #declare password list which will contain the individual characters
    #password list must contain at least one of uppercase letter, lowercase letter, digits and symbols
    passwordList = []

    passwordList.append(random.choice(string.ascii_uppercase))
    passwordList.append(random.choice(string.ascii_lowercase))
    passwordList.append(random.choice(string.digits))
    passwordList.append(random.choice(string.punctuation))

    #subtract 4 if the length specified is greater than four. This will fill in the rest of the password
    for index in range(length - 4):

        randomChoice = random.choice([0, 1, 2, 3])

        if randomChoice == 0:
            passwordList.append(random.choice(string.ascii_uppercase))
        elif randomChoice == 1:
            passwordList.append(random.choice(string.ascii_lowercase))
        elif randomChoice == 2:
            passwordList.append(random.choice(string.digits))
        else:
            passwordList.append(random.choice(string.punctuation))

    random.shuffle(passwordList)
    return ''.join(passwordList)


print(generateRandomPassword(12))