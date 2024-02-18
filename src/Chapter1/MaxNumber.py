import random

#Small program to check the largest number in a list
def find_max(numbers):

    #initialize max_num variable to zero
    max_num = 0

    #iterate through list passed into function
    for number in numbers:
        
        #first number will become max on first iteration, then other iterations will check the new max
        if number > max_num:
            max_num = number

    return max_num

def generate_randomlist(listLength):

    randomList = []

    for i in range(0, listLength):

        randomList.append(random.randint(0, 200000))

    return randomList

numbers = generate_randomlist(10)

print(numbers)

print('The largest number in the list is: ' + str(find_max(numbers)))