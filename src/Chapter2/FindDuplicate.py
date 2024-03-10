#Program which finds if provided item is duplicated within provided list
#Returns none if item is not duplicated

#Algorithm has a linear time complexity of O(n) as it can iterate
#over how many items are in list

#Space complexity is O(n) linear time since we might have to store each value in holding list
#Holding list is linear to the items in list variable

def find_duplicate(list):

    holdingList = []

    for item in list:

        if item in holdingList:
            return item
    
        holdingList.append(item)

    return "None"


duplicate = find_duplicate([1, 2, 3, 4, 6, 6])

if duplicate == "None":
    print("No duplicate found in list...")
else:
    print("Duplicate found in list is: " + str(duplicate))