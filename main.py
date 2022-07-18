


'''

Exercise 10a

 Write a function, mysum_bigger_than , that works the same as mysum , except that
it takes a first argument that precedes *args . That argument indicates the
threshold for including an argument in the sum. Thus, calling mysum_bigger
_than(10, 5, 20, 30, 6) would return 50 —because 5 and 6 aren’t greater than
10 . This function should similarly work with any type and assumes that all of the
arguments are of the same type. Note that > and < work on many different types
in Python, not just on numbers; with strings, lists, and tuples, it refers to their
sort order.

'''

def mysum_bigger_than(threshold, *items):
    if not items:  # If items is empty
        return ()
    else: 
        output = items[0]
        for item in items[1:]:
            if item > threshold:
                output += item
        return output

print(mysum_bigger_than([1, 2, 3, 2], *([1, 2, 3, 4], [1, 2, 4, 5], [4, 6, 7])))
print(mysum_bigger_than('error', *('today', '0', 'car', '4', '19')))
print(mysum_bigger_than((14, 79, 110), *((1231, 12, 136), (5828, 853, 968))))
print(mysum_bigger_than(185, *(135, 5917, 9186, -293)))
print(mysum_bigger_than(5, *()))