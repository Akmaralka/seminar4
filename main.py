from mytree import heap_sort

with open("words.txt") as file:
    arr = file.readlines()

words = []

for i in range(len(arr)-1):
    arr[i] = arr[i][:len(arr[i])-1]
    words.append(arr[i])

print(words)
heap_size = len(words)
heap_sort(words, heap_size)
print(words)
