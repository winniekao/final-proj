import random
g = open("user2no",'w')
a = 0
with open("user_id_temp") as f:
	for line in f:
		g.write(str(a))
		g.write('\n')
		a = a+1
g.close()

