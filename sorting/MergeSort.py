#MergeSort [5, 0, 1, 4, 2, 6]

def mergersort(arr):
	return mergesort_rec(arr, 0, len(arr)-1)

def mergesort_rec(arr, left, right):
    mid = (left + right)//2
    if left>=right:
        return [arr[left]]
    
    lefthalf = mergesort_rec(arr, mid+1, right)
    righthalf = mergesort_rec(arr, left, mid) 
    return merge(lefthalf, righthalf)


def merge(lefthalf, righthalf):
    ll = len(lefthalf)
    lr = len(righthalf)
    new = []
    pl = 0
    pr = 0
    for i in range(lr+ll):
        if pl < ll and pr < lr:
            if lefthalf[pl] < righthalf[pr]:
                new.append(lefthalf[pl])
                pl+=1
            else:
                new.append(righthalf[pr])
                pr+=1
        if pl < ll:
            new.append(lefthalf[pl])
            pl+=1
        if pr < lr:
            new.append(righthalf[pr])
            pr+=1
    return new