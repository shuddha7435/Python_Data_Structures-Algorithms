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

if __name__ == "__main__":
        h = [None, 19, 7 , 12, 3, 5, 17, 10, 1, 2]
        print(h)
        max_heapify(h, 9, 3)
        print(h)
        print()
        h = [None, 1, 2, 3]
        print(h)
        max_heapify(h, 3, 1)
        print(h)

def build_max_heap(heap):
    heap_size = len(heap) - 1

    for i in range(heap_size//2, 0, -1):
        max_heapify(heap, heap_size, i)

if __name__ == "__main__":
        heap = [None, 12, 7, 1, 3, 10, 17, 19, 2, 5]
        print("Before building heap", heap)
        build_max_heap(heap)
        print("After building heap", heap)
