g = open("rel.user.test","w")

with open("user2no") as f:
	for line in f:
		user = line.split()
		user_no = user[0] 
#		print user_no
		with open("trip2no") as h:
			for line in h:
				g.write(user_no)
				g.write('\n')
g.close

