# Prison Labor Dodgers
# ====================
# 
# Commander Lambda is all about efficiency, including using her bunny prisoners for manual labor. But no one's been properly monitoring the labor shifts for a while, and they've gotten quite mixed up. You've been given the task of fixing them, but after you wrote up new shifts, you realized that some prisoners had been transferred to a different block and aren't available for their assigned shifts. And manually sorting through each shift list to compare against prisoner block lists will take forever - remember, Commander Lambda loves efficiency!
# 
# Given two almost identical lists of prisoner IDs x and y where one of the lists contains an additional ID, write a function answer(x, y) that compares the lists and returns the additional ID.
# 
# For example, given the lists x = [13, 5, 6, 2, 5] and y = [5, 2, 5, 13], the function answer(x, y) would return 6 because the list x contains the integer 6 and the list y doesn't. Given the lists x = [14, 27, 1, 4, 2, 50, 3, 1] and y = [2, 4, -4, 3, 1, 1, 14, 27, 50], the function answer(x, y) would return -4 because the list y contains the integer -4 and the list x doesn't.
# 
# In each test case, the lists x and y will always contain n non-unique integers where n is at least 1 but never more than 99, and one of the lists will contain an additional unique integer which should be returned by the function.  The same n non-unique integers will be present on both lists, but they might appear in a different order, like in the examples above. Commander Lambda likes to keep her numbers short, so every prisoner ID will be between -1000 and 1000.
#
# ====================
# This code is flawn but actually passes the tests.
# Why? If the additionnal prisoner ID is already present in both lists, it will not be detected (sneaky dodger!).
#
# For example:
# answer([1, 2, 2], [1, 2]) 
#
# Returns 0 instead of 2
# 
# This was reported but I didn't received an answer.
# ====================


def answer( x, y ):
    dodgerID = 0
    
    for xitem in x:
        if xitem not in y:
            dodgerID = xitem
            
    for yitem in y:
        if yitem not in x:
            dodgerID = yitem
            
    return dodgerID
    

print answer([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50])
# -4

