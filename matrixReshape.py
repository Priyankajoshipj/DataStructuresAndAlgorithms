def matrixReshape(nums, r, c):
	oldr = len(nums)
    if oldr == 0:
        return nums
    oldc = len(nums[0])
    if r * c != oldr * oldc:
        return nums

    res = []
    out = [[0 for i in range(c)] for j in range(r)]

    for i in range(oldr):
        for j in range(oldc):
            res.append(nums[i][j])
    index = 0
    for i in range(r):
        for j in range(c):
            out[i][j] = res[index]
            index += 1
    return out