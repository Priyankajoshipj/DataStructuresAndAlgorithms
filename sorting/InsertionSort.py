#Insertion Sort
# How is it differet than Selection sort:
	# In selection sort we stick with a position and find the suitable item for that position by scaning the array
	# that is we start with the last index and fill it with the largest element in the array and move toward the index 0
	# While in Insertion sort, we pick an element a (starting at index1) and find where it goes, that is it's home.
#[5, 6, 1, 4, 2, 6]
# First pass no swap since is less than 6
def insertionSort(arr):
	n = len(arr)

	for i in range(1,n):
		j = i - 1
		temp = arr[i]
		while (j > -1 and temp < arr[j]):
			arr[j+1] = arr[j]
			arr[j] = temp
			j -=1
		i += 1
	return arr


