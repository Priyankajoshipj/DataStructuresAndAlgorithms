def get_parent(i):
    return (i-1)//2

def get_leftcihld(i):
    return (2*i) + 1

def get_rightcihld(i):
    return (2*i) + 2

def percolate_down(i, n, heap):
    while i < n:
        left = get_leftcihld(i)
        right = get_rightcihld(i)
        if left < n and right <n:
            a, ai = heap[right], right
            b, bi = heap[left], left
        elif left < n:
            a, ai = heap[left], left
            b, bi = float('-inf'), n
        elif right < n:
            a, ai = heap[right], right
            b, bi = float('-inf'), n
        else:
            return heap
        if heap[i] == max(heap[i], a, b):
                return heap
        elif heap[i] < a:
            heap[i], heap[ai] = heap[ai], heap[i]
            heap = percolate_down(ai, n, heap)
        elif heap[i] < b:
            heap[i], heap[bi] = heap[bi], heap[i]
            heap = percolate_down(bi, n, heap)
    return heap

def heapify(heap, n):
    mid = n//2
    i = mid
    while (i > -1):
        heap = percolate_down(i, n, heap)
        i -= 1
    return heap

def heapsort(arr):

    n = len(arr)
    heap = heapify(arr, n)
    i = n-1
    while( i > -1):
        heap[0], heap[i] = heap[i], heap[0]
        heap = percolate_down(0, i-1, heap)
        i -= 1
    return heap