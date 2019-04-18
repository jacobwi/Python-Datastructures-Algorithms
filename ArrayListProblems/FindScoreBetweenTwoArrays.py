'''
    Compares each element in a list with its opposite element at same index with another list
    This method accomplish that with O(n) time complexitiy
'''

def compareScores(a, b):
    result = [0, 0]
    for i in a:
  
        if i > b[(a.index(i))]:
            result[0] += 1
        elif i < b[(a.index(i))]:
            result[1] += 1
    return result

print([5, 6, 7], [3, 6, 10])