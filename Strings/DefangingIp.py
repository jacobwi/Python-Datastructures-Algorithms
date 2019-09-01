'''
    O(n) time complexity
    approach type: concat a string whenver the condition is true
'''
def defangIPaddr(address: str) -> str:
    output = ""
    for i in range(len(address)):
        if (address[i] == '.'):
            output += "[.]"
        else:
            output += address[i]
        
    return output

print(defangIPaddr("1.1.1.1"))