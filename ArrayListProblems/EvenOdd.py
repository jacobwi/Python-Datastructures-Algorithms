'''
    This algorithm will solve an array problem where we want to take an array of integers
    then sort them to show even numbers first then odd second and vice versa.
'''

def even_then_odd(arrayOfNums):
    even = 0
    odd = len(arrayOfNums) - 1
    while even < odd:
        if arrayOfNums[even] % 2 == 0:
            even += 1
        else:
            arrayOfNums[even], arrayOfNums[odd] =  arrayOfNums[odd],  arrayOfNums[even]
            odd -= 1
    return(arrayOfNums)

def odd_then_even(arrayOfNums):
    even = 0
    odd = len(arrayOfNums) - 1
    while even < odd:
        if arrayOfNums[even] % 2 != 0:
            even += 1
        else:
            arrayOfNums[odd], arrayOfNums[even] =  arrayOfNums[even], arrayOfNums[odd]
            odd -= 1
    return(arrayOfNums)
arr = [4, 3, 2, 7, 8, 12, 34, 31, 36, 100]
print(even_then_odd(arr))
print(odd_then_even(arr))