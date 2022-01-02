# Quick sorting algorithms

# Strategy: Recurisive method

# Time complexity:
# - worst case: O(n^2)
# - average: O(n log n)


from typing import List


def quick_sort(elements: List[int]) -> List[int]:
    ...
    # check the base case
    if len(elements) <= 1: return elements
    
    # get the last element from the list
    pivot = elements.pop()

    elements_lower = []
    elements_higher = []
    
    for element in elements:
        if element < pivot:
            elements_lower.append(element)
        else:
            elements_higher.append(element)
    
    # call the method and use the pivot values    
    return quick_sort(elements_lower) + [pivot] + quick_sort(elements_higher)


element = [5,43,11,2,1,67,4,98]
print(quick_sort(elements=element))







