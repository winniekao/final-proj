import random
g = open("trip2no",'w')
a = 0
with open("trip_id_temp") as f:
	for line in f:
		g.write(str(a))
		g.write('\n')
		a = a+1
g.close()

