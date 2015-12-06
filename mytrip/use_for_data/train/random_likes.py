import random
g = open("likes",'w')

with open("trip_id_temp") as f:
	for line in f:
		likes = random.randint(1, 5)
		g.write(str(likes))
		g.write('\n')
g.close()

