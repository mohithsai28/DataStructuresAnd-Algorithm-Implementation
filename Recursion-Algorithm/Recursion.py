
def recursion(global_counter):
    print(global_counter)
    if(global_counter>3):
        return "Done"
    global_counter += 1
    return recursion(global_counter)


#011234
def fibanocci(n):
    if(n<2):
        return n
    return fibanocci(n-1)+fibanocci(n-2)

def reversestring(string):
    n=len(string)
    if(n==1):
        return string[0]
    n-=1
    print(string[n],end='')
    return reversestring(string[0:n])




print(reversestring("Mohith"))
#print(fibanocci(8))
# print(recursion(0))


