class Heap():
    def __init__(self):
        self.heap = []

    def __str__(self):
        return '[' + ', '.join(str(x) for x in self.heap) + ']'

    def parent(self, i):
        return (i - 1) / 2

    def insert(self, element):
        if element not in self.heap:
            self.heap.append(element)

    def length(self):
        return(len(self.heap))

    def delete(self, element):
        self.heap.pop(element)

    def heapify(self, heap_size, i):
        left = 2 * i
        right = left + 1
        if left < heap_size and self.heap[left] > self.heap[i]:
            high = left
        else:
            high = i
        if right < heap_size and self.heap[right] > self.heap[high]:
            high = right
        if i != high:
            self.heap[i], self.heap[high] = self.heap[high], self.heap[i]
            self.heapify(heap_size, high)

    def create_max_heap(self):
        heap_size = len(self.heap)
        for i in range(heap_size//2 - 1, 0, -1):
            self.heapify(heap_size, i)

    def heap_sort(self, heap_size):
        self.create_max_heap()
        for i in range(heap_size - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            heap_size = heap_size - 1
            self.heapify(heap_size, 0)
