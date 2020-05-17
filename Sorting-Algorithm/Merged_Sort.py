def mergesort(list1,list2):
    li=[]
    i,j=0,0
    if len(list1)==0 and len(list2)==0:
        return li
    if len(list1)==0 and len(list2)!=0:
        return list2
    if len(list1)!=0 and len(list2)==0:
        return list1
    while i<len(list1) and j<len(list2):
        print(i,j)
        if list1[i]<list2[j]:
            li.append(list1[i])
            i+=1
        else:
            li.append(list2[j])
            j+=1
    li+=list1[i:]+list2[j:]
    return li


print(mergesort([0,3,4,31],[4,6,30]))

