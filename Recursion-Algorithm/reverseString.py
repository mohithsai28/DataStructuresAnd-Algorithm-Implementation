#Mohith

def reversestring(s):
    array=[]
    length=len(s)
    for i in range(length):
        array.insert(i,s[length-1])
        length-=1
    string1=''.join(array)
    return string1


print(reversestring("Mohith"))
