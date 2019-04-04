'''
    Assuming the integer is positive and has no sign we can do below
'''
def reverse(x):
    print(int(str(x)[::-1]))

def reverseAny(x):
    answer = 0
    if x >= 0:
        answer = int(str(x)[::-1]) 
    else:
        answer = -int(str(-x)[::-1])

    return answer

reverse(123)
print(reverseAny(-432))