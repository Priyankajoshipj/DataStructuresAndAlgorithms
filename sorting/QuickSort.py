#QuickSort
#[5, 0, 1, 4, 2, 6]  left = 0 right = 5
#pivot 6, No swaps in pass1, now left = 0 right = 3 and 6 to 5 - second one is base case
# quicksort on left = 0 to right = 4
#pivot 2, [0, 1, 2, 4, 5, 6] left part 0 to 1 and right part 3, 4
#both base cases return sorted arr
#Let last element be the pivot
def quicksort(arr):
	return quicksort_rec(arr, 0, len(arr)-1)

def quicksort_rec(arr, left, right):
    if left >= right:
        return arr
    pivot = right
    j = left
    lastswapped = left
    
    while j < right:
        if arr[j] < arr[pivot]:
            if j != lastswapped:
                arr[j], arr[lastswapped] = arr[lastswapped], arr[j]  
            lastswapped +=1
        j+=1
    if pivot != lastswapped:
        arr[lastswapped], arr[pivot] = arr[pivot], arr[lastswapped]
    arr = quicksort_rec(arr,left,lastswapped-1)
    arr = quicksort_rec(arr,lastswapped +1,right)
    return arr
