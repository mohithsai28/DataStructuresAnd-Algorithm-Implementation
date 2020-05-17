

def bublesort(num):
    for k in range(len(num)):
        for m in range(len(num)-1):
            if(num[m]>num[m+1]):
                temp=num[m]
                num[m]=num[m+1]
                num[m+1]=temp
            else:
                continue
    return num

def selectionsort(num):
    for n in range(len(num)):
        small=n
        temp=num[n]
        for m in range(n+1,len(num)):
            if(num[small]>num[m]):
                small=m
        num[n] = num[small]
        num[small]=temp


    return num


def insertion_sort(num):
    length=len(num)
    i=1
    end=num[0]
    while i<length:
        if num[i]<end:
            x=num.pop(i)
            for j in range(0,i):
                if x<num[j]:
                    num.insert(j,x)
                    break
        end=num[i]
        i+=1
    return num

def mergesort(num):
    if len(num)==1:
        return num
    length=len(num)
    mid=length//2
    left=num[:mid]
    right=num[mid:]
    return merge(mergesort(left),mergesort(right))

def merge(left, right):
  result = []
  leftIndex = 0
  rightIndex = 0
  while leftIndex<len(left) and rightIndex<len(right):
      if left[leftIndex]<right[rightIndex]:
          result.append(left[leftIndex])
          leftIndex+=1
      else:
          result.append(right[rightIndex])
          rightIndex+=1
  return result+left[leftIndex:]+right[rightIndex:]


def partition(array,low,high):
    i = low
    pivot = array[high]

    for j in range(low,high):
        if array[j] < pivot:
            array[i],array[j] = array[j],array[i]
            i+=1
    array[i],array[high] = array[high],array[i]
    return i

def quickSort(array, low, high):
    if low < high:
        pi = partition(array,low,high)

        quickSort(array,low,pi-1)
        quickSort(array,pi+1, high)







#num=[99,44,6,2,1,5,63,87,283,4,0]
#print(mergesort(num))
#print(insertion_sort(num))
#print(bublesort(num))
#print(selectionsort(num))

arr=[99,44,62,1,5,80]
# arr = ['k','g','r','f','Q','A','a','z','c']
n = len(arr)-1
quickSort(arr,0,n)
print(arr)
# print(sorted(arr))