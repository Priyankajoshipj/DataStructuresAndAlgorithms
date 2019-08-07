#Selection Sort
# How is it differet than Insertion sort:
	# In Insertion sort, we pick an element a (starting at index1) and find where it goes, that is it's home.
	# While In selection sort we stick with a position and find the suitable item for that position by scaning the array
	# that is we start with the last index and fill it with the largest element in the array and move toward the index 0
#[5, 6, 1, 4, 2, 6]
# pass1 : i = 5, j goes from 0 to 5,k =1 swap arr[i] and arr[k] arr [5, 6, 1, 4, 2, 6]
# pass2 : i = 4, j goes from 0 to 4,k = 1 swap arr [5, 2, 1, 4, 5, 6]
# pass2 : i = 3, j goes from 0 to 3,k = 0 swap arr [4, 2, 1, 5, 6, 6]
# pass3 : i = 2, j goes from 0 to 2,k = 0 swap arr [1, 2, 4, 5, 6, 6]
# pass4 : i = 1, j goes from 0 to 1,k = 1 no swap
# pass5 : i = 0, j goes from 0 to 0,k = 0

def selectionSort(arr):
	n = len(arr)
	for i in range(n-1,-1,-1):
		k = 0
		j = k+1

		while(j <= i):
			if (arr[j] > arr[k]):
				k = j
			j += 1

		if k != i:
			arr[k], arr[i] = arr[i], arr[k]
	return arr
