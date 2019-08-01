def gameOfLife(board):
	m=len(board)
	n=len(board[0])
	copy=[[board[i][j] for j in range(n)] for i in range(m) ]
	for i in range(m):
		neighbours=[(1,0),(0,-1),(1,-1),(-1,-1),(1,1),(0,1),(-1,0),(-1,1)]
		countones=0
		for j in range(n):
			r= i+neighbours[0]
			c= jneighbours[1]

			if((r>=0 and r<m) and (c>=0 and c<n) and board[r][c]==1):
				countones+=1

			if (copy[i][j]==1 and (countones<2 or countones>3)):
				board[i][j]=0
			if(copy[i][j]==0 and countones==3):
				board[i][j]=1

def generateParentheses(n):
	
	if n==0:
		return ['']
	ans=[]

	for i in range(n):
		for left in self.generateParentheses(i)
			for right in self.generateParentheses(n-1-i):
				ans.append('({}){}'.format(left,right))
	return ans

def swapNodes(head):
	node=head
	while(node.next!=None):
		node= swap(node)
	return head
def swap(head):
	n=head
	head=n.next
	head.next=n.next.next
	n.next=n
	return head


def longestpalindrome(s,left,right):
    if(left>right):
        return 0,False
    if(right==left):
        return 1,True
    if(right-left==1):
        if(s[right]==s[left]):
            return 2,True
        else:
            return 1,False
    if(s[left]==s[right]):
        length,ispal=longestpalindrome(s,left+1,right-1)
        if(ispal):
            return 2+length,True
        else:
            return length,ispal
    else:
        leftsub,ispal=longestpalindrome(s,left+1,right)
        rightsub,ispal=longestpalindrome(s,left,right-1)
        return max(leftsub,rightsub)

def minWindSub(s,t):
	diction={}
	minlen=0
	for i in t:
	    if(i not in diction.keys()):
	        diction[i]=1
	    else:
	        diction[i]+=1
	count={}
	left=0
	right=1
	while(right<len(s)):
		if(s[left] not in diction.keys()):
			left+=1
			right+=1
			continue
		else:
			count[s[left]]=1
		if(right not in diction.keys()):
			right+=1
			continue
		else:
			if(s[right] not in count.keys()):
				s[right]=1
			else:
				s[right]+=1
		if(count==diction):
			if(right-left<minlen):
				minlen=right-left
				count={}
			left+=1
			right=left+1

	return minlen

#----------------
s='azjskfzts'
t='zs'
diction={s:1,z:1}
minlen=3
count={s:1}
left=3
right=

 https://raw.githubusercontent.com/mongodb/docs-assets/primer-dataset/primer-dataset.json
 --------------

 def min_coins_dp(cents):
 	coins=[25, 10, 1]
 	return helper(cents,0, coins)


 def helper(cents,i,coins):
 	if cents<coins[i]
 		return sys.MAXINT
 	return min(helper(cents,i+1,coins),cents/coins[i]+helper(cents%coins[i],i+1,coins))

