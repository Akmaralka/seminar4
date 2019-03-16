def heapify(words, heap_size, i):
    left = 2 * i
    right = left + 1
    if left < heap_size and words[left] > words[i]:
        high = left
    else:
        high = i
    if right < heap_size and words[right] > words[high]:
        high = right
    if i != high:
        words[i], words[high] = words[high], words[i]
        heapify(words, heap_size, high)


def create_max_heap(words):
    heap_size = len(words)
    for i in range(heap_size//2 - 1, 0, -1):
        heapify(words, heap_size, i)


def heap_sort(words, heap_size):
    create_max_heap(words)
    for i in range(heap_size - 1, 0, -1):
        words[0], words[i] = words[i], words[0]
        heap_size = heap_size - 1
        heapify(words, heap_size, 0)
