from binarytree import tree

def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def max_heapify(heap, heap_size, i):
    l = left(i)
    r = right(i)

    if l <= heap_size and heap[l] > heap[i]:
        largest = l
    else:
        largest = i

    if r <= heap_size and heap[r] > heap[largest]:
        largest = r

    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap, heap_size, largest)

def build_max_heap(heap):
    heap_size = len(heap) - 1

    for i in range(heap_size//2, 0, -1):
        max_heapify(heap, heap_size, i)

def heap_sort(heap):
    build_max_heap(heap)
    heap_size = len(heap) - 1

    for i in range(heap_size, 1 , -1):
        heap[1], heap[i] = heap[i], heap[1]
        heap_size -= 1
        max_heapify(heap, heap_size, 1)

if __name__ == "__main__":
        heap = [None, 12, 7, 1, 3, 10, 17, 19, 2, 5]
        print("Before sorting", heap)
        heap_sort(heap)
        print("After sorting", heap)
