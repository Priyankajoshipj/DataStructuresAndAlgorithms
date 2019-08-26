def circles(info):
	def check_circles(xa,ya,ra,xb,yb,rb):
		if xa == 0 and ya == 0 and xb == 0 and yb == 0:
			return "Concentric"

		if xa == 0 and xb == 0:
			c1 = ya
			c2 = yb

		elif ya == 0 and yb == 0:
			c1 = xa
			c2 = xb

		if abs(c1 - c2) == abs(ra - rb):
			return "Touching"

		elif c1 == c2:
			return "Concentric"

		elif abs(c1 - c2) < (ra + rb):
			return "Intersecting"

		elif abs(c1 - c2) > (ra + rb):
			return "Disjoint-Outside"

		else:
			p1a, p2a = c1 - ra, c1 + ra
			p1b, p2b = c2 - rb, c2 + rb
			if (p1a < p1b and p2a > p2b) or (p1b < p1a and p2b > p2a):
				return "Disjoint-Inside"

	result = []
	for i in range(len(info)):
		xa,ya,ra,xb,yb,rb = info[i][0], info[i][1], info[i][2], info[i][3], info[i][4], info[i][5] 
		result.append(check_circles(xa,ya,ra,xb,yb,rb))

	return result
	
	


info = [[0,5,9,0,9,7], [0,15,11,0,20,16]]
print(circles(info))
