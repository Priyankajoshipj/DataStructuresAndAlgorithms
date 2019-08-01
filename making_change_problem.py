# [1, 2, 5] amt 11 coins->3
# Both approaches work and were accepted on LeetCode for Question 322

def change_making_dp_top_down(coins,amount):
    arr = {}
    def helper(coins,amount,arr):
        if (amount == 0):
            return 0
        if amount < 0:
            return float('inf')
        if amount in arr.keys():
            return arr[amount]
        minc = float('inf')
        for c in coins:
            if amount >= c:
                num = helper(coins,amount - c,arr)
                if num >=0 and num<minc:
                    minc = 1+num
        arr[amount] = minc               

        return arr[amount] 
    c = helper(coins,amount,arr)
    return c if c != float('inf') else -1

#coins available = [1, 2, 5]
#amount		0 1 2 3 4 5 6 7 
#min_coins	0 1 1 2 2 1 
def change_making_dp_bottoms_up(coins,amount):
	arr = [ amount + 1 for j in range(amount+1) ]
	arr[0] = 0

	for i in range (1,amount+1):
		minc = arr[i]
		for c in coins:
			if i >= c:
				minc = min (minc, arr[i-c]+1)
		arr[i] = minc
	return arr[amount] if arr[amount] != amount+1 else -1

if __name__ == "__main__":
	coins = [1, 2, 5]
	amount = 11
	print("Bottoms_Up_DP ",change_making_dp_bottoms_up(coins,amount))
	print("Top_down_DP ",change_making_dp_top_down(coins,amount))