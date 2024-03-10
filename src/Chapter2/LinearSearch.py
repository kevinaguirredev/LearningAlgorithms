#Program to find whether item exists within provided list
#If item is found in list, return the index of item in array
#Return -1 if not found in list

#Time complexity will be O(n) linear time
#Space complexity will be O(1) constant time

def linear_search(list, item):

    for index in range(len(list)):

        if list[index] == item:
            return index
        
    return -1
        
    
    
position = linear_search([1, 3, 5, 7, 9], 5)

print('The item was found at position: '  + str(position))