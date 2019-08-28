#Amazon Phone Screen interview question
def Parking_service(slots, actions):
	# slots has an input for small medium and large availability
	ticket = 0
	tickets = {}
	out = []
	for i in range(len(actions)):
		
		if actions[i][0] == "arrival":
			if actions[i][1] == "small":
				slot = 0
			elif actions[i][1] == "medium":
				slot = 1
			else:
				slot = 2
			if slots[slot] > 0:
				ticket += 1
				out.append(ticket)
				tickets[ticket] = slot
				slots[slot] -= 1
			else:
				out.append('reject')
		else:
			slot = tickets[actions[i][1]]
			del tickets[actions[i][1]]
			slots[slot] += 1
	return out

res = Parking_service([1,1,2],[("arrival", "small"),("arrival", "large"), ("arrival", "medium"), ("arrival", "large"), ("arrival", "medium")])
print (res)
res1 = Parking_service([1,1,2],[("arrival", "small"),("arrival", "large"), ("arrival", "medium"), ("arrival", "large"),("depart", 3), ("arrival", "medium")])
print(res1)
#Output 
# [1, 2, 3, 4, 'reject']
# [1, 2, 3, 4, 5]
