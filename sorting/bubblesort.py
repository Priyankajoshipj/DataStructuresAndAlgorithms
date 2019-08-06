#[5, 6, 1, 4, 2, 6]
#pass1: 5,1,4,2,6,6
#pass2: 1,4,2,5,6,6
#pass3: 1,2,4,5,6,6
#pass4: No swap -> break

def bubblesort(arr):
    n = len(arr)
    for i in range(n-1):
       # print(i) to check if the array is already sorted this solution stops after one pass
        swap = False
        for j in range (n-i-1):
            if arr[j] > arr[j+1]:
                swap = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swap:
            break
    return arr