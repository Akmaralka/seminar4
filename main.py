from mytree import Heap

with open("words.txt") as file:
    arr = file.readlines()

heap = Heap()

for i in range(len(arr)-1):
    arr[i] = arr[i][:len(arr[i])-1]
    heap.insert(arr[i])

print(heap)
heap_size = heap.length()
heap.heap_sort(heap_size)
print(heap)
