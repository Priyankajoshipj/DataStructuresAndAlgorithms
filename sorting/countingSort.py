#[5, 6, 1, 4, 2, 6]
# counter = [0, 1, 1, 0, 1, 1, 2]
# runningsum = [0, 1, 2, 2, 3, 4, 6]
# placement = [1, 2, 4, 3, 5, 6]
def countingSort(arr, k):
    counter = [0]*(k+1)
    n = len(arr)
    for i in range(n):
        counter[arr[i]] += 1
    runningsum = [0]*(k+1)
    # You can remove runningsum 
    # and update counter to store running sum instead, to save memory
    # I added this for clarity
    runningsum[0] = counter[0]
    for i in range(1, n):
        runningsum[i] = runningsum[i-1]+counter[i]

    placement = [0] * n
    for i in range(n-1,-1,-1):
        runningsum[ arr[i] ] -= 1
        lastindex = runningsum[ arr[i] ]
        placement[lastindex] = arr[i]
    return placement
