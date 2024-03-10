#Program to sum all elements in a list and return total sum
#Program takes one list of N elements

#Program will have a time linear complexity of O(n) as
#loop will operate for a total number of items in list

#Space complexity is O(1) as there will be only one total variable
#regardless of how many items there are

def sum_elements(list):

    total = 0

    for item in list:

        total += item

    return total


total = sum_elements([1, 2, 3, 4, 5])

print("Total is: " + str(total))