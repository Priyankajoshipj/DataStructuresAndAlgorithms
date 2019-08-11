#searching in a sorted 2-D matrix
''' eg: matrix =[1, 2, 3]
                [4, 5, 6]
                [7, 8, 9] 
        look for 5 in matrix
        start with row r check if it falls in between matrix[r][0] and matrix[r][n-1] where n is no. of cols
        if yes then do a binary search to lookup the element
'''
def search_in_sorted_matrix(matrix, target):
    if not matrix:
        return False
    rows = len(matrix)
    col = len(matrix[0])
    if col == 0:
        return False
    for i in range(rows):
        if target < matrix[i][col-1] and target > matrix[i][0]:
            col_i = bin_search(matrix[i], col, target)
            # return [i,col_i] if col_i != -1 else -1 // in case you need the exact position of the element found
            return True if col_i != -1 else False
        elif target == matrix[i][col-1] or target == matrix[i][0]:
            return True
    return False

def bin_search(arr, n, target):
    left = 0
    right = n-1
    if left == right:
        return left if target == arr[left] else -1
    while(left <= right):
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1