import heapq

# Min Heap
li = [1,3,4,7,9]
heapq.heapify(li)
print(li)
heapq.heappush(li, 5)
print(li)
heapq.heappop(li)
print(li)
heapq.heappushpop(li, 6)
print(li)
heapq.heapreplace(li,8)
print(li)
print(heapq.nlargest(3,li))
print(heapq.nsmallest(3,li))


# Max Heap
values = [1,3,4,7,9]
li = [(-1*i) for i in values]
heapq.heapify(li)
print(li)
heapq.heappush(li, -5)
print(li)
heapq.heappop(li)
print(li)
heapq.heappushpop(li, -6)
print(li)
heapq.heapreplace(li,-8)
print(li)
print(heapq.nlargest(3,li))
print(heapq.nsmallest(3,li))
