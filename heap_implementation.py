class heap:
    def __init__(self):
        self.heap = []
        self.size = 0
    def heapify(self):
        n = self.size
        mid = n//2
        i = mid
        while (i > -1):
            self.percolate_down(i)
            i -= 1
        return self.heap
    def percUp(self):
        i = self.size - 1
        while i // 2 > -1 :
          if self.heap[i] > self.heap[i // 2]:
             tmp = self.heap[i // 2]
             self.heap[i // 2] = self.heap[i]
             self.heap[i] = tmp
          i = i // 2 if i != 0 else -1
    def heappush(self, item):
        self.heap.append(item)
        self.size += 1
        return self.percUp()
    
    def heapop(self):
        popped = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.size = self.size - 1
        self.percolate_down(0)
        return popped
    def get_parent(self, i):
        return (i-1)//2

    def get_leftcihld(self, i):
        return (2*i) + 1

    def get_rightcihld(self, i):
        return (2*i) + 2

    def percolate_down(self, i):
        n = self.size
        while i < self.size:
            left = self.get_leftcihld(i)
            right = self.get_rightcihld(i)
            if left < n and right <n:
                a, ai = self.heap[right], right
                b, bi = self.heap[left], left
            elif left < n:
                a, ai = self.heap[left], left
                b, bi = float('-inf'), n
            elif right < n:
                a, ai = self.heap[right], right
                b, bi = float('-inf'), n
            else:
                return 
            if self.heap[i] == max(self.heap[i], a, b):
                    return 
            elif self.heap[i] < a:
                self.heap[i], self.heap[ai] = self.heap[ai], self.heap[i]
                self.percolate_down(ai)
            elif self.heap[i] < b:
                self.heap[i], self.heap[bi] = self.heap[bi], self.heap[i]
                self.percolate_down(bi)
        return 

h = heap()
h.heappush(0)
h.heappush(1)
h.heappush(5)
h.heapop()

print(h.heap)
h.heappush(4)
h.heappush(8)
h.heappush(3)

print(h.heap)