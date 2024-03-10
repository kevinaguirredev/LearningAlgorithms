#Program that bubble sorts list in ascending order

#For this algorithm, space complexity is O(1) as we are not creating any other lists

#Time complexity is O(n^2) quadratic because we need to compare each item

def bubble_sort(list):

    n = len(list)

    for i in range(n):
        
        for j in range (0, n - i - 1):
            
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


bubble_sort([5, 1, 4, 8, 2])